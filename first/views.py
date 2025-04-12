from django.shortcuts import render

# Create your views here.


def index_page(request):
    context = {}
    return render(request, 'index.html', context)


def about_page(request):
    context = {}
    return render(request, 'about.html', context)


def methodology_page(request):
    context = {}
    return render(request, 'methodology.html', context)


def contacts_page(request):
    context = {}
    return render(request, 'contacts.html', context)