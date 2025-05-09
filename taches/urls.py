from django.urls import path
from .views import TacheListView, TacheCreateView, TacheUpdateView, TacheDeleteView

urlpatterns = [
    path('', TacheListView.as_view(), name='tache_list'),
    path('ajouter/', TacheCreateView.as_view(), name='tache_add'),
    path('modifier/<int:pk>/', TacheUpdateView.as_view(), name='tache_edit'),
    path('supprimer/<int:pk>/', TacheDeleteView.as_view(), name='tache_delete'),
]
