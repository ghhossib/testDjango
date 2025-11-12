from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.hello,name='home'),
    path('', views.get,name='categories'),
    path('<int:category_id>/', views.show,name='category'),
    path('update/<int:category_id>/', views.update,name='update_category'),
    path('add/<int:category_id>/', views.add,name='category_create'),
    path('delete/<int:category_id>/', views.delete,name='delete_category'),

]
