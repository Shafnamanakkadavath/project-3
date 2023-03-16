from django.contrib import admin
from django.urls import path,include
from .import views
app_name='moveiapp'

urlpatterns = [


    path('', views.film, name='film'),
    path('film/<int:movei_id>/',views.detail,name='detail'),
    path('add/',views.addmovei,name='addmovei'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]