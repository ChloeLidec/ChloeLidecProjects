"""
URL configuration for GestionSoutien project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import include, path
from user import views as usv

# app_name = ''
urlpatterns = [
    path("user/",include("user.urls")),
    path("qcm/",include("QCM.urls")),
    path("sondages/",include("Sondages.urls")),
    path('admin/', admin.site.urls),
    path('suivi/', include('Suivi.urls')),
    path('parametres/', include('Param.urls')),
    path('disponibilites/', include('Dispos.urls')),
    path('accueil/', views.accueil, name='accueil'),
    path('', views.accueil, name='acceuil'),
]
