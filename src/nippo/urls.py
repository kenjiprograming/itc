from django.urls import path
from .views import nippoDetailView, NippoListView, nippoCreateFormView, nippoUpdateView, nippoDeleteView, ImageUploadView
 
urlpatterns = [
  path('', NippoListView.as_view(), name='nippo-list'),
  path('detail/<int:pk>', nippoDetailView, name='nippo-detail'),
  path('create/', nippoCreateFormView.as_view(), name='nippo-create'),
  path('update/<int:pk>/', nippoUpdateView, name='nippo-update'),
  path('delete/<int:pk>/', nippoDeleteView, name='nippo-delete'),
  path('image-upload/', ImageUploadView.as_view(), name='image-upload'),
]
