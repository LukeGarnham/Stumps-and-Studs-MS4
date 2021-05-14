from django.shortcuts import render


def contact(request):
    """ Contact Stumps & Studs form. """
    template = 'contact/contact.html'
    context = {}

    return render(request, template, context)
