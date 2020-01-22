from django.urls import path
from MainApp import views
urlpatterns = [
    
    path('',views.index,name='index')
]