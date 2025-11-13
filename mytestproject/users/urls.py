from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.get,name='login'),
    path('users/', views.login_user,name='users'),


]
