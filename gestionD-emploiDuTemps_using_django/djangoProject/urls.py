"""
URL configuration for djangoProject project.

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
from django.contrib import admin
from django.urls import path
from scheduleManagement import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #acceuil
    path('', views.acceuil , name = ''),

    #users
    path('users_home/', views.user_home , name = 'users_home'),
    path('add_utilisateur/', views.add_utilisateur, name='add_utilisateur'),
    path('users_list/', views.list_utilisateurs, name='users_list'),
    path('delete_utilisateur/<int:user_id>/', views.delete_utilisateur, name='delete_utilisateur'),
    path('edit_utilisateur/<int:user_id>/', views.edit_utilisateur, name='edit_utilisateur'),


    #cours
    path('cours_home/', views.cours_home , name="cours_home"),
    path('add_cours/', views.add_cours, name='add_cours'),
    path('cours_list/', views.cours_list, name='cours_list'),
    path('delete_cours/<int:c_id>/', views.delete_cours, name='delete_cours'),
    path('edit_cours/<int:cours_id>/', views.edit_cours, name='edit_cours'),


    #salle
    path('salle_home/', views.salle_home , name="salle_home"),
    path('add_salle/', views.add_salle, name='add_salle'),
    path('salles_list/', views.salle_list, name='salles_list'),
    path('delete_salle/<int:salle_id>/', views.delete_salle, name='delete_salle'),
    path('edit_salle/<int:salle_id>/', views.edit_salle, name='edit_salle'),


    
    #emploi du temps
    path('emploi_home/', views.emlpoi_home , name="emploi_home"),
    path('add_emploi/', views.add_emploi_du_temps, name='add_emploi'),
    path('emploi_list/', views.emploi_list, name='emploi_list'),
    path('delete_emploi/<int:emploi_id>/', views.delete_emploi, name='delete_emploi'),
    path('edit_emploi/<int:emploi_id>/', views.edit_emploi, name='edit_emploi'),


    



    



]
