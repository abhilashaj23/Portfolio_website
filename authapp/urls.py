from django.urls import path
from authapp import views

urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('login', views.Handlelogin,name='Handlelogin'),
    path('logout', views.Handlelogout,name='Handlelogout'),
    
]