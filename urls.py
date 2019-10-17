from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('login', views.login, name='login'),
    path('do_login', views.do_login, name='do_login'),
    
    ]