from django.urls import path
from .views import nippoDetailView, nippoListView, nippoCreateView, nippoUpdateView
 
urlpatterns = [
  path('', nippoListView, name='nippo-list'),
  path('detail/<int:pk>', nippoDetailView, name='nippo-detail'),
  path('create/', nippoCreateView, name='nippo-create'),
  path('update/<int:pk>/', nippoUpdateView, name='nippo-update'),
]