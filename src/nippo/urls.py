from django.urls import path
from .views import NippoListView, NippoDetailView, NippoCreateModelFormView, NippoUpdateModelFormView, nippoDeleteView, ImageUploadView
 
urlpatterns = [
  path('', NippoListView.as_view(), name='nippo-list'),
  path('detail/<int:pk>', NippoDetailView.as_view(), name='nippo-detail'),
  path('create/', NippoCreateModelFormView.as_view(), name='nippo-create'),
  path('update/<int:pk>/', NippoUpdateModelFormView.as_view(), name='nippo-update'),

  path('delete/<int:pk>/', nippoDeleteView, name='nippo-delete'),
  path('image-upload/', ImageUploadView.as_view(), name='image-upload'),
]
