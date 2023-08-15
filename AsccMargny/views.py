from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def evenement_view(request):
    return render(request, 'evenement.html')

def contact_view(request):
    return render(request, 'contact.html')

def vieduclub_view(request):
    return render(request, 'vieduclub.html')

def partenaire_view(request):
    return render(request, 'partenaire.html')

def equipe_view(request):
    return render(request, 'equipe.html')

def archive_view(request):
    return render(request, 'archive.html')

def r1_view(request):
    return render(request, 'r1.html')