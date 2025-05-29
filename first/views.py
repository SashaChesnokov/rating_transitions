import csv
from django.shortcuts import render
from django.conf import settings
from first.models import Scores
import os
# Create your views here.


# views.py
import csv
from django.shortcuts import render
from django.conf import settings
import os


def index_page(request):
    databases = Scores.objects.all().order_by('place')

    return render(request, 'index.html', {'databases': databases})


def about_page(request):
    context = {}
    return render(request, 'about.html', context)


def methodology_page(request):
    context = {}
    return render(request, 'methodology.html', context)


def contacts_page(request):
    context = {}
    return render(request, 'contacts.html', context)