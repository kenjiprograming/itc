from django.urls import path
from .views import NippoDetailView, NippoListView, NippoCreateFormView, nippoUpdateView, nippoDeleteView, ImageUploadView
 
urlpatterns = [
  path('', NippoListView.as_view(), name='nippo-list'),
  path('detail/<int:pk>', NippoDetailView.as_view(), name='nippo-detail'),
  path('create/', NippoCreateFormView.as_view(), name='nippo-create'),
  path('update/<int:pk>/', nippoUpdateView, name='nippo-update'),
  path('delete/<int:pk>/', nippoDeleteView, name='nippo-delete'),
  path('image-upload/', ImageUploadView.as_view(), name='image-upload'),
]
