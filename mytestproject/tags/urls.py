from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='tags'),
    path('add/', views.add, name='add-tag'),
    path('<int:id>/', views.show, name='tag'),
    path('<int:id>/delete/', views.delete, name='delete-tag'),
    path('<int:id>/update/', views.update, name='update-tag'),
]