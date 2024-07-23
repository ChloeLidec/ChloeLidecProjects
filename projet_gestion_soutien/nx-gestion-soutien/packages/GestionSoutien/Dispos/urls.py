from . import views
from django.urls import  path

app_name = 'Dispos'
urlpatterns = [
    path('vue/', views.dispo,name='vue'),
    path('gerer/', views.gerer_dispos,name='gerer'),
]
