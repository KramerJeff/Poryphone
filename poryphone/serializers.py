from rest_framework import serializers
from .models import (Type, Role, Category, Target, RecruitMethod, Trainer, SyncPair, Item, ItemQuantity, Move,
    SyncPairMove, Passive, SyncPairPassive, SyncMove, Pokemon)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ("id", "name")  # TODO change to ["name"]??


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
        fields = ("id", "name")  # TODO change to ["name"]


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ("id", "name", "description")


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "description", "obtain_method", "img_path")


class ItemQuantitySerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=False)

    class Meta:
        model = ItemQuantity
        fields = ("id", "item", "quantity")


class MoveSerializer(serializers.ModelSerializer):
    type = TypeSerializer(many=False)
    category = serializers.SerializerMethodField(method_name="get_category_name")

    def get_category_name(self, instance):
        return instance.category.name

    class Meta:
        model = Move
        fields = ("id", "name", "description", "type", "category",
                  "power", "accuracy", "target", "energy_cost", "num_uses")


class SyncPairMoveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name="get_name")
    move = MoveSerializer(many=False)
    unlock_requirements = ItemQuantitySerializer(many=True)

    def get_name(self, instance):
        pokemon_name = instance.syncpair.pokemon.get(evo_stage=1).name
        trainer_name = instance.syncpair.trainer.name
        return trainer_name + ' & ' + pokemon_name

    class Meta:
        model = SyncPairMove
        fields = ("id", "name", "move", "unlock_requirements")


#class PassiveSerializer
#class SyncPairPassiveSerializer

class SyncMoveSerializer(serializers.ModelSerializer):
    syncpair_name = serializers.SerializerMethodField(method_name="get_syncpair_name")

    def get_syncpair_name(self, instance):
        syncpair_name = instance.syncpair.name
        return syncpair_name

    class Meta:
        model = SyncMove
        fields = ("id", "name", "type", "category", "power", "target", "syncpair_name")


class SyncPairSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(many=False)
    recruit_method = RecruitMethodSerializer(many=False)
    pokemon = serializers.SerializerMethodField(method_name="get_pokemon")
    syncpair_name = serializers.SerializerMethodField(method_name="get_name")
    syncpair_moves = serializers.SerializerMethodField(method_name="get_moves")
    # syncpair_passive = SyncPairPassiveSerializer()

    class Meta:
        model = SyncPair
        fields = ("id", "syncpair_name", "trainer", "pokemon",
            "syncpair_moves", "base_potential", "recruit_method")

    def get_pokemon(self, instance):
        pokemon = instance.pokemon.all().order_by('evo_stage')
        return PokemonSerializer(pokemon, many=True).data

    def get_name(self, instance):
        pokemon_name = instance.pokemon.get(evo_stage=1).name
        trainer_name = instance.trainer.name
        return trainer_name + ' & ' + pokemon_name

    def get_moves(self, instance):
        spmoves = instance.spmoves.all() #order_by?
        #moves = []
        #for spmove in spmoves:
        #    moves.append(spmove.move)
        #get rid of name
        return SyncPairMoveSerializer(spmoves, many=True).data

class PokemonSerializer(serializers.ModelSerializer):
    type = TypeSerializer(many=True)
    weakness = TypeSerializer(many=False)

    class Meta:
        model = Pokemon
        fields = ("id", "name", "description", "type",
                  "weakness", "is_mega", "evo_stage")
