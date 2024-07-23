from . import views
from django.urls import path

app_name = 'QCM'
urlpatterns = [
    path('', views.res_qcm, name='resultats_qcm'),
]

htmx_views = [
    path('get-bandeau/',views.get_bandeau,name='get-bandeau'),
    path('ajouter-eleve/<str:num_etu>',views.ajouter_eleve,name='ajouter-eleve'),
    path('delete-row/',views.delete_row,name='delete-row'),
    path('get-matiere/',views.get_matiere,name='get-matiere'),
]

urlpatterns += htmx_views