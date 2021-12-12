from django.urls import path
from .import views

urlpatterns = [

    path('createform',views.createform,name='createform'),
    path('success',views.success,name='success')
]