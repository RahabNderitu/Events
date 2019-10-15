from django.urls import path

from . import views


app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('dashboard', views.dashboard, name='dashboard'),
    
    

]