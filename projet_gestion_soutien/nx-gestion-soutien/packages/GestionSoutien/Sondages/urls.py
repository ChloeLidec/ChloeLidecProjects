from . import views
from django.urls import path

app_name = 'Sondages'
urlpatterns = [
   
    path('', views.res_sond, name='resultats_sond'),
   
]
