from django.db import models
from django.contrib.postgres.fields import ArrayField


# Pokemon Types e.g. Grass, Electric, etc.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )
    img_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


# Role of Sync Pairs - e.g. Striker, Support, Tech
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )
    img_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


# Category of Moves - e.g. Special, Physical, Status Effect
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    img_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


# Target for Moves
class Target(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.name

# Sync Move (not quite the same as a Move, wasted columns)
# Passive (not quite the same as Move, wasted columns)


# Recruit method for Sync Pairs
class RecruitMethod(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name


# Pokemon Trainer
class Trainer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# Sync Pair - Pokemon Family + Trainer
class SyncPair(models.Model):
    id = models.AutoField(primary_key=True)
    # This is the name of the base form of the Pokemon
    name = models.CharField(
        max_length=255,
        null=False,
        blank=True, unique=True, default='Unown')
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        related_name='syncpair',
        null=True, blank=True)
    base_potential = models.IntegerField(null=True, blank=True, default=3)
    recruit_method = models.ForeignKey(
        RecruitMethod,
        on_delete=models.SET_NULL,
        null=True, blank=True)

    class Meta:
        unique_together = ["name", "trainer"]
        ordering = ["trainer"]

    def __str__(self):
        return "{} - {}".format(self.trainer, self.name)

# The items available in the game
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    obtain_method = models.CharField(max_length=255, null=True, blank=True)
    img_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

# The item and quantity needed for a specific unlock requirement
class ItemQuantity(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        related_name='iqs', null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ["item", "quantity"]

    def __str__(self):
        return "{} x {}".format(self.item.name, self.quantity)

# A move "belongs" to either a Trainer or a Pokemon
# - ultimately belonging to a Sync Pair
class Move(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    power = ArrayField(models.IntegerField(), null=True, blank=True, size=2)
    accuracy = models.IntegerField(null=True, blank=True)
    target = models.ForeignKey(
        Target,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    energy_cost = models.IntegerField(null=True, blank=True)
    num_uses = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

# The moves of a specific Sync Pair
class SyncPairMove(models.Model):
    id = models.AutoField(primary_key=True)
    move = models.ForeignKey(
        Move,
        on_delete=models.SET_NULL,
        related_name='spmoves',
        null=True,
        blank=True
    )
    syncpair = models.ForeignKey(
        SyncPair,
        on_delete=models.SET_NULL,  # This might warrant a cascade since SyncPairMove is a specific SyncPair's move
        related_name='spmoves',
        null=True,
        blank=True
    )
    unlock_requirements = models.ManyToManyField(
        ItemQuantity,
        related_name='spmoves',
        blank=True
    )

    class Meta:
        unique_together = ["move", "syncpair"]
        ordering = ["syncpair"]

    def __str__(self):
        return "{} - {}".format(self.syncpair.name, self.move.name)

class Passive(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

class SyncPairPassive(models.Model):
    id = models.AutoField(primary_key=True)
    passive = models.ForeignKey(
        Passive,
        on_delete=models.SET_NULL,
        related_name='sppassive',
        null=True,
        blank=False
    )
    syncpair = models.ForeignKey(
        SyncPair,
        on_delete=models.SET_NULL,  # This might warrant a cascade since SyncPairMove is a specific SyncPair's move
        related_name='sppassive',
        null=True,
        blank=True
    )    
    unlock_requirements = models.ManyToManyField(
        ItemQuantity,
        related_name='sppassive',
        blank=True
    )

    def __str__(self):
        return "{} - {}".format(self.syncpair.name, self.passive.name)

class SyncMove(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )   
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    power = ArrayField(models.IntegerField(), null=True, blank=True, size=2)
    target = models.ForeignKey(
        Target,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    syncpair = models.ForeignKey(
        SyncPair,
        on_delete=models.SET_NULL,
        related_name='syncmoves',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

# Used to represent a Pokemon
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.ManyToManyField(
        Type,
        related_name='%(class)s_type',
        blank=True
    )
    weakness = models.ForeignKey(
        Type,
        related_name='%(class)s_weakness',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_mega = models.BooleanField(null=False, blank=False)
    evo_stage = models.IntegerField(null=False, blank=False, default=1)
    syncpair = models.ForeignKey(
        SyncPair,
        on_delete=models.SET_NULL,
        related_name='pokemon',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
