from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        """ Customise placeholders, add classes, remove auto-generated
        labels and set autofocus on the first field (Phone Number). """
        super().__init__(*args, **kwargs)
        # Create a dictionary of placeholders where:
        # key = field, value = placeholder.
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'message': 'Message',
        }

        # Set the autofocus to the full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Loop through all fields.
        for field in self.fields:
            # If the field is required, add asterix to placeholder.
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = f'{placeholders[field]}'
            # Set the placeholder attribute to
            # the placeholder created above.
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove the field labels.
            self.fields[field].label = False
