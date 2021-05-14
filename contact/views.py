from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ Contact Stumps & Studs form. """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print('Succes')
            messages.success(request, 'Thank you for your message.  \
                Someone will respond via email soon.')
            print('Succes - after message')
        else:
            messages.error(request, 'Message failed.  Please ensure the \
                form is valid.')

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
