from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about_me(request):
    record = About.objects.order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        'about/about.html',
        {
            'about': record,
            'collaborate_form': collaborate_form
        }
    )
