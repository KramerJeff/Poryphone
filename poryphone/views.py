from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import status
from .models import Trainer, Move, Pokemon, SyncPair, Type
from .serializers import TrainerSerializer, MoveSerializer, PokemonSerializer, SyncPairSerializer, TypeSerializer #
import json
# Create your views here.
class ListTrainerView(generics.ListAPIView):
  """
  Provides a get method handler
  """
  queryset = Trainer.objects.all()
  serializer_class = TrainerSerializer

class TrainerViewSet(viewsets.ViewSet):

  """
  Provides a get method handler
  """
  queryset = Trainer.objects.all()
  serializer_class = TrainerSerializer

  def id(self, request, *args, **kwargs):
    try:
      trainer = self.queryset.get(pk=kwargs["pk"])
      return Response(TrainerSerializer(trainer).data)
    except Trainer.DoesNotExist:
      return Response(
        data={
          "message": "Trainer with id: {} does not exist".format(kwargs["pk"])
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
          "message": "Trainer with name: {} does not exist".format(kwargs["name"])
        },
        status=status.HTTP_404_NOT_FOUND
      )      

class ListTypeView(generics.ListAPIView):
  """
  Provides a get method handler
  """
  queryset = Type.objects.all()
  serializer_class = TypeSerializer

class ListMoveView(generics.ListAPIView):
  """
  Provides a get method handler
  """
  queryset = Move.objects.all()
  serializer_class = MoveSerializer

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
          "message": "Pokemon with id: {} does not exist".format(kwargs["pk"])
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
          "message": "Pokemon with name: {} does not exist".format(kwargs["name"])
        },
        status=status.HTTP_404_NOT_FOUND
      )      

class ListSyncPairView(generics.ListAPIView):
  queryset = SyncPair.objects.all()
  serializer_class = SyncPairSerializer  


class SyncPairViewSet(viewsets.ViewSet):

  """
  Provides a get method handler
  """
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
          "message": "Sync pair with id: {} does not exist".format(kwargs["pk"])
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
          "message": "Sync pair with name: {} does not exist".format(kwargs["name"])
        },
        status=status.HTTP_404_NOT_FOUND
      )