"""Views for the About app, including the about_me page and collaboration form."""

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Handle the About page.

    - GET:
        * Fetch the latest About instance (for body text + profile image).
        * Render the page with an empty collaboration form.
    - POST:
        * Validate and save the collaboration form.
        * Show a success message and redirect back to the About page (PRG pattern).
    """
    # Prepare the form depending on the request method
    if request.method == "POST":
        # Bind POST data to the form
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            # Save the request to the DB
            collaborate_form.save()

            # Flash a success message visible on the next page load
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond within 2 working days.",
            )

            # Redirect to avoid form resubmission if the user refreshes the page
            return redirect("about")
    else:
        # Unbound (empty) form on initial GET
        collaborate_form = CollaborateForm()

    # Fetch the latest About instance to display on the page
    # If none exists, the template will show a simple fallback
    about_instance = About.objects.order_by("-updated_on").first()

    # Render the template with both the About data and the collaboration form
    return render(
        request,
        "about/about.html",
        {
            # used for body + profile image (with fallback in template)
            "about": about_instance,
            "collaborate_form": collaborate_form,  # crispy-rendered form
        },
    )
