from django.urls import path
from .views import ListTrainerView, TrainerViewSet,
ListMoveView, ListPokemonView, PokemonViewSet,
ListSyncPairView, SyncPairViewSet, ListTypeView,
ListItemView, ListRoleView

urlpatterns = [
    path('trainers/', ListTrainerView.as_view(), name='trainer-all'),
    path('trainers/<int:pk>/',
         TrainerViewSet.as_view({'get': 'id'}), name='trainer-detail'),
    path('trainers/<name>/',
         TrainerViewSet.as_view({'get': 'get_name'}), name='trainer-name'),
    path('moves/', ListMoveView.as_view(), name='move-all'),
    path('syncpairs/', ListSyncPairView.as_view(), name='syncpair-all'),
    path('syncpairs/<int:pk>/',
         SyncPairViewSet.as_view({'get': 'id'}), name='syncpair-detail'),
    path('syncpairs/<name>/',
         SyncPairViewSet.as_view({'get': 'get_name'}), name='syncpair-name'),
    path('pokemon/',
         ListPokemonView.as_view(), name='pokemon-all'),
    path('pokemon/<int:pk>/',
         PokemonViewSet.as_view({'get': 'id'}), name='pokemon-detail'),
    path('pokemon/<name>/',
         PokemonViewSet.as_view({'get': 'get_name'}), name='pokemon-name'),
    path('types/', ListTypeView.as_view(), name='type-all'),
    path('items/', ListItemView.as_view(), name='item-all'),
    path('roles/', ListRoleView.as_view(), name='role-all')
]
