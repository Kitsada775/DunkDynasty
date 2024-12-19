# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='register'),
    path('home', views.home, name='home'), 
    path('', views.login_view, name='login'),
]
