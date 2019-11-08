from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import status
import json
from .models import Trainer, Move, Pokemon, SyncPair, Type, Role, Category, Target, RecruitMethod, Item, ItemQuantity, SyncPairMove
from .serializers import TrainerSerializer, MoveSerializer, SyncPairSerializer, TypeSerializer, RoleSerializer, CategorySerializer, TargetSerializer, RecruitMethodSerializer, ItemSerializer, ItemQuantitySerializer, SyncPairMoveSerializer, PokemonSerializer


class ListTypeView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ListRoleView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ListCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListTargetView(generics.ListAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class ListRecruitMethodView(generics.ListAPIView):
    queryset = RecruitMethod.objects.all()
    serializer_class = RecruitMethodSerializer


class ListTrainerView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerViewSet(viewsets.ViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    def id(self, request, *args, **kwargs):
        try:
            trainer = self.queryset.get(pk=kwargs["pk"])
            return Response(TrainerSerializer(trainer).data)
        except Trainer.DoesNotExist:
            return Response(
                data={
                    "message":
                        "Trainer with id: {} does not exist"
                        .format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def get_name(self, request, *args, **kwargs):
        try:
            trainer = self.queryset.get(name__iexact=kwargs["name"])
            return Response(TrainerSerializer(trainer).data)
        except Trainer.DoesNotExist:
            return Response(
                data={
                    "message":
                        "Trainer with name: {} does not exist"
                        .format(kwargs["name"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListSyncPairView(generics.ListAPIView):
    queryset = SyncPair.objects.all()
    serializer_class = SyncPairSerializer


class SyncPairViewSet(viewsets.ViewSet):
    queryset = SyncPair.objects.all()
    serializer_class = SyncPairSerializer

    def id(self, request, *args, **kwargs):
        try:
            syncpair = self.queryset.get(pk=kwargs["pk"])
            pokemon = syncpair.pokemon.all()
            data = {}
            data['syncpair'] = SyncPairSerializer(syncpair).data
            data['pokemon'] = {}
            for i in range(len(pokemon)):
                data['pokemon'][i] = PokemonSerializer(pokemon[i]).data
            return Response(data)
        except SyncPair.DoesNotExist:
            return Response(
                data={
                    "message":
                        "Sync pair with id: {} does not exist"
                        .format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
            except Exception as e:
                return Response(
                    data={
                        "message": str(e)
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

    def get_name(self, request, *args, **kwargs):
        try:
            syncpair = self.queryset.get(name__iexact=kwargs["name"])
            pokemon = syncpair.pokemon.all()
            data = {}
            data['syncpair'] = SyncPairSerializer(syncpair).data
            data['pokemon'] = {}
            for i in range(len(pokemon)):
                data['pokemon'][i] = PokemonSerializer(pokemon[i]).data
            return Response(data)
        except SyncPair.DoesNotExist:
            return Response(
                data={
                    "message":
                        "Sync pair with name: {} does not exist"
                        .format(kwargs["name"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListMoveView(generics.ListAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer


class ListItemView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ListItemQuantityView(generics.ListAPIView):
    queryset = ItemQuantity.objects.all()
    serializer_class = ItemQuantitySerializer


class ListSyncPairMoveView(generics.ListAPIView):
    queryset = SyncPairMove.objects.all()
    serializer_class = SyncPairMoveSerializer


class ListPokemonView(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonViewSet(viewsets.ViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def id(self, request, *args, **kwargs):
        try:
            pokemon = self.queryset.get(pk=kwargs["pk"])
            return Response(PokemonSerializer(pokemon).data)
        except Pokemon.DoesNotExist:
            return Response(
                data={
                    "message":
                        "Pokemon with id: {} does not exist"
                        .format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def get_name(self, request, *args, **kwargs):
        try:
            pokemon = self.queryset.get(name__iexact=kwargs["name"])
            return Response(PokemonSerializer(pokemon).data)
        except Pokemon.DoesNotExist:
            return Response(
                data={
                    "message":
                        "Pokemon with name: {} does not exist"
                        .format(kwargs["name"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
