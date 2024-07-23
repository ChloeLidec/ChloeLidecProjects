from . import views
from django.contrib import admin
from django.urls import include, path

app_name = 'Suivi'
urlpatterns = [
    # path('suivi_etudiant/', views.suivi_etu, name='suivi_etudiant'),
    path('suivi_etudiant/<str:num_etu>', views.suivi_etu, name='suivi_etudiant'),
    path('suivi_general/', views.suivi_gen, name='suivi_general'),
]
