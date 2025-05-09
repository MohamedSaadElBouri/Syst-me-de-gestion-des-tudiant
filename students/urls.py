from django.urls import path
from . import views

urlpatterns = [
    path('download/', views.download_page, name='download_page'),
    path('', views.index, name='index'),
    path('student/<int:id>/', views.view_student, name='view_student'),
    path('add_student/', views.add_student, name='add_student'),
    path('guid/<int:id>/', views.view_guid, name='view_guid'),
    path('calendar/', views.calendar, name='calendar'),
    path('formulaire/<int:id>/', views.view_formulaire, name='view_formulaire'),
    path('login/', views.connexion, name='connexion'),
    path('signup/', views.inscription, name='inscription'),
    path('logout/', views.deconnexion, name='deconnexion'),
]
