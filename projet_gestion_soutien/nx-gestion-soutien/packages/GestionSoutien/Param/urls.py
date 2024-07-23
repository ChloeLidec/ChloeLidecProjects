from django.urls import path
from . import views

app_name = 'Param'
urlpatterns = [
    path('', views.param, name='parametres'),
    path('get-profs/',views.get_profs,name='get-profs'), 
    path('creneau/',views.creneau,name='creneau'), 
    path('suppr-soutien/<int:pk>',views.suppr_soutien,name='suppr-soutien'),]    


