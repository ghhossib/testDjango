from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.hello,name='home'),
    path('', views.get,name='categories'),
    path('<int:id>/', views.show,name='category'),
    path('update/<int:id>/', views.update,name='update_category'),
    path('add/', views.add,name='category_create'),
    path('delete/<int:id>', views.delete,name='delete_category'),

]
