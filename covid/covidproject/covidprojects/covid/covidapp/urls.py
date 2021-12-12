from  .import views
from django.urls import path
app_name='covidapp'
urlpatterns = [

    path('',views.main,name='main'),
    path('<slug:c_slug>',views.getplace,name='getplace'),
]