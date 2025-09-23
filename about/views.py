from django.shortcuts import render
from .models import About

# Create your views here.


def about_me(request):
    record = About.objects.order_by('-updated_on').first()
    return render(request, 'about/about.html', {'about': record})
