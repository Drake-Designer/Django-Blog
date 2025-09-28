"""Views for the About app, including the about_me page and collaboration form."""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Handle the About page:
    - GET: display about info and collaboration form.
    - POST: validate and save collaboration form, then redirect with success message.
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond within 2 working days.",
            )
            return redirect("about")
    else:
        collaborate_form = CollaborateForm()

    about_instance = About.objects.order_by(
        "-updated_on").first()  # pylint: disable=no-member
    return render(
        request,
        "about/about.html",
        {
            "about": about_instance,
            "collaborate_form": collaborate_form,
        },
    )
