from django.shortcuts import render

from .models import Contact
from .forms import ContactForm


def contact(request):
    """ Contact Stumps & Studs form. """

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
