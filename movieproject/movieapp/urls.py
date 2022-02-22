from django.contrib import admin
from django.urls import path,include
from . import views
app_name='movieapp'
urlpatterns = [


    path('', views.fun,name='fun'),

    path('movie/<int:movie_id>/', views.details,name='details'),
    path('add/',views.register,name='register'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('del/<int:id>/',views.delete,name='delete')

]