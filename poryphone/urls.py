from django.urls import path
from .views import (ListTypeView, ListRoleView, ListCategoryView, ListTargetView, ListRecruitMethodView,
    ListTrainerView, TrainerViewSet, ListMoveView, ListPokemonView, PokemonViewSet, ListSyncPairView,
    SyncPairViewSet, ListItemView, ListItemQuantityView, ListSyncPairMoveView)

urlpatterns = [
    path('types/', ListTypeView.as_view(), name='type-all'),
    path('roles/', ListRoleView.as_view(), name='role-all'),
    path('categories/', ListCategoryView.as_view(), name='category-all'),
    path('targets/', ListTargetView.as_view(), name='target-all'),
    path('recruitmethods/', ListRecruitMethodView.as_view(), name='recruit-method-all'),
    path('trainers/', ListTrainerView.as_view(), name='trainer-all'),
    path('trainers/<int:pk>/',
         TrainerViewSet.as_view({'get': 'id'}), name='trainer-detail'),
    path('trainers/<name>/',
         TrainerViewSet.as_view({'get': 'get_name'}), name='trainer-name'),
    path('syncpairs/', ListSyncPairView.as_view(), name='syncpair-all'),
    path('syncpairs/<int:pk>/',
         SyncPairViewSet.as_view({'get': 'id'}), name='syncpair-detail'),
    path('syncpairs/<name>/',
         SyncPairViewSet.as_view({'get': 'get_name'}), name='syncpair-name'),
    path('moves/', ListMoveView.as_view(), name='move-all'),
    path('items/', ListItemView.as_view(), name='item-all'),
    path('itemquantities/', ListItemQuantityView.as_view(), name='item-quantity-all'),
    path('syncpairmoves/', ListSyncPairMoveView.as_view(), name='sync-pair-move-all'),
    path('pokemon/',
         ListPokemonView.as_view(), name='pokemon-all'),
    path('pokemon/<int:pk>/',
         PokemonViewSet.as_view({'get': 'id'}), name='pokemon-detail'),
    path('pokemon/<name>/',
         PokemonViewSet.as_view({'get': 'get_name'}), name='pokemon-name'),
    
]
