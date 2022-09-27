from . import views
from django.urls import path

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('button',views.button,name='button'),
    path('form',views.form,name='form'),
    path('application', views.application,name='application'),
    path('logout',views.logout,name='logout')

]