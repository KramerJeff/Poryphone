from django.db import models
from django.contrib.postgres.fields import ArrayField

class Type(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False, blank=False)
  img_path = models.CharField(max_length=255, null=True, blank=True)
  
  def __str__(self):
    return self.name

class Role(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False, blank=False)
  img_path = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.name

class Category(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False, blank=False)
  img_path = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.name

class Target(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False, blank=False)

  def __str__(self):
    return self.name

class Move(models.Model):
  id = models.AutoField(primary_key=True)
  #name of the move
  name = models.CharField(max_length=255, null=False)
  description = models.CharField(max_length=255, null=True, blank=True)
  type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
  power = ArrayField(models.IntegerField(), null=True, blank=True, size=2)
  accuracy = models.IntegerField(null=True, blank=True)
  target = models.ForeignKey(Target, on_delete=models.SET_NULL, null=True, blank=True)
  cost = models.IntegerField(null=True, blank=True) #should this be a single column?
  is_energy = models.BooleanField(null=False, blank=False, default=True)

  def __str__(self):
    return self.name

class RecruitMethod(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False)

  def __str__(self):
    return self.name


#Sync Move (subclass of move)
# Create your models here.
class Trainer(models.Model):
  id = models.AutoField(primary_key=True)
  #trainer name
  name = models.CharField(max_length=255, null=False)
  description = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.name

#describes the Sync Pair
class SyncPair(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=True, blank=True, default='Unown')
  role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
  trainer = models.OneToOneField(Trainer, on_delete=models.SET_NULL, related_name='syncpair', null=True, blank=True)
  base_potential = models.IntegerField(null=True, blank=True, default=3)
  moves = models.ManyToManyField(Move, related_name='%(class)s_move', null=True, blank=True)
  recruit_method = models.ForeignKey(RecruitMethod, on_delete=models.SET_NULL, null=True, blank=True)
  
  def __str__(self):
    return "{} - {}".format(self.name, self.trainer)


#class Passive(models.Model):
class Pokemon(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255, null=False)
  type = models.ManyToManyField(Type, related_name='%(class)s_type', blank=True)
  weakness = models.ForeignKey(Type, related_name='%(class)s_weakness', on_delete=models.SET_NULL, null=True, blank=True)
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



