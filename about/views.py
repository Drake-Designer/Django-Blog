from django.shortcuts import render
from .models import About

# Create your views here.


def about_page(request):
    record = About.objects.first()
    return render(request, 'about/about.html', {'about': record})
