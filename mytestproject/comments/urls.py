from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='comments'),
    path('add/', views.add, name='add-comment'),
    path('<int:id>/', views.show, name='comment'),
    path('<int:id>/delete/', views.delete, name='delete-comment'),
    path('<int:id>/update/', views.update, name='update-comment'),
]