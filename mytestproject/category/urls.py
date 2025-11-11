from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.hello,name='home'),
    path('category/', views.categories,name='category'),
    path('category/<int:category_id>', views.categories,name='one_category'),
    path('category/add/', views.category_create,name='category_create'),

]
