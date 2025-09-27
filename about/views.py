from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )
            return redirect("about")

    else:
        collaborate_form = CollaborateForm()

    about = About.objects.order_by("-updated_on").first()
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
