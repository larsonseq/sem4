from django.urls import path
from . import views

urlpatterns = [ 
      
    path('', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('next/', views.next, name='next'),
]