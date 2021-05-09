from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Customise placeholders, add classes, remove auto-generated
        labels and set autofocus on the first field (Phone Number). """
        super().__init__(*args, **kwargs)
        # Create a dictionary of placeholders where:
        # key = field, value = placeholder.
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town/City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
        }

        # Set the autofocus to the full name field
        # self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Loop through all fields.
        for field in self.fields:
            if field != 'default_country':
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
