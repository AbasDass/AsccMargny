from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('evenement/', views.evenement_view),
    path('contact/', views.contact_view),
    path('vieduclub/', views.vieduclub_view),
    path('partenaire/', views.partenaire_view),
    path('equipe/', views.equipe_view),
    path('archive/', views.archive_view),

]
