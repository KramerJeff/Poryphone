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

# Sync Move (subclass of move)
# Passive (subclass of move?)


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

    def __str__(self):
        return self.name


# Sync Pair - Pokemon Family + Trainer
class SyncPair(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        null=False,
        blank=True, unique=True, default='Unown')
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True)
    trainer = models.OneToOneField(
        Trainer,
        on_delete=models.SET_NULL,
        related_name='trainer',
        null=True, blank=True)
    base_potential = models.IntegerField(null=True, blank=True, default=3)
    recruit_method = models.ForeignKey(
        RecruitMethod,
        on_delete=models.SET_NULL,
        null=True, blank=True)

    class Meta:
        unique_together = ["name", "trainer"]

    def __str__(self):
        return "{} - {}".format(self.name, self.trainer)


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
    # Should these be a single column?
    cost = models.IntegerField(null=True, blank=True)
    is_energy = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.name


# The items available in the game
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    obtain_method = models.CharField(max_length=255, null=True, blank=True)
    img_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ItemQuantity(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        related_name='item', null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ["item", "quantity"]

    def __str__(self):
        return "{} x {}".format(self.item.name, self.quantity)


# The moves of a specific Sync Pair
class SyncPairMove(models.Model):
    id = models.AutoField(primary_key=True)
    move = models.ForeignKey(
        Move,
        on_delete=models.SET_NULL,
        related_name='move',
        null=True,
        blank=True
    )
    syncpair = models.ForeignKey(
        SyncPair,
        on_delete=models.SET_NULL,
        related_name='syncpair',
        null=True,
        blank=True
    )
    unlock_requirements = models.ManyToManyField(
        ItemQuantity,
        related_name='items',
        blank=True
    )

    class Meta:
        unique_together = ["move", "syncpair"]

    def __str__(self):
        return "{} - {}".format(self.syncpair.name, self.move.name)


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
        ordering = ['id']

    def __str__(self):
        return self.name
