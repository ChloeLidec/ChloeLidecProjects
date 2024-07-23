from . import views
from django.urls import path

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('register/', views.register, name='register'),
    path('new_mdp/', views.new_mdp, name='new-mdp'),
    
]
