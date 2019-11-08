from rest_framework import serializers
from .models import Trainer, Move, Pokemon, SyncPair, Type, Role, Category, Target, RecruitMethod, Item, SyncPairMove, ItemQuantity

class TypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Type
    fields = ("id", "name") #TODO change to ["name"]??

class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role
    fields = ("id", "name", "img_path")

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ("id", "name", "img_path")

class TargetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Target
    fields = ("id", "name")

class RecruitMethodSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecruitMethod
    fields = ("id", "name") #TODO change to ["name"]

class TrainerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Trainer
    fields = ("id", "name", "description")

class SyncPairSerializer(serializers.ModelSerializer):
  trainer = TrainerSerializer(many=False)
  recruit_method = RecruitMethodSerializer(many=False)
  class Meta:
    model = SyncPair
    fields = ("id", "name", "trainer", "base_potential", "recruit_method")

class MoveSerializer(serializers.ModelSerializer):
  type = TypeSerializer(many=False)
  class Meta:
    model = Move
    fields = ("id", "name", "description", "type", "category", "power", "accuracy", "target", "cost", "is_energy")

class PokemonSerializer(serializers.ModelSerializer):
  type = TypeSerializer(many=True)
  weakness = TypeSerializer(many=False)
  class Meta:
    model = Pokemon
    fields = ("id", "name", "description", "type", "weakness", "is_mega", "evo_stage")

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ("id", "name", "description", "obtain_method", "img_path")

class ItemQuantitySerializer(serializers.ModelSerializer):
  item = ItemSerializer(many=False)
  class Meta:
    model = ItemQuantity
    fields = ("id", "item", "quantity")

class SyncPairMoveSerializer(serializers.ModelSerializer):
  syncpair = SyncPairSerializer(many=False)
  move = MoveSerializer(many=False)
  unlock_requirements = ItemQuantitySerializer(many=True)
  class Meta:
    model = SyncPairMove
    fields = ("id", "syncpair", "move", "unlock_requirements")