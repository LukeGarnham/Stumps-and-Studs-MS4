from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ Contact Stumps & Studs form. """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'message': request.POST['message'],
            }
            form.save()

            # Send the user an email acknowledging their message.
            cust_email = request.POST['email'],
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'contact_message': contact_message})
            body = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'contact_message': contact_message,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )

            messages.success(request, 'Thank you for your message.  \
                Someone will respond via email soon.')
        else:
            messages.error(request, 'Message failed.  Please ensure the \
                form is valid.')

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
