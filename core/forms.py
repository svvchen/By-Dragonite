from django import forms
from .models import Subscriber
from django.core.exceptions import ValidationError

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Enter your email:  ',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    email.widget.attrs.update({'autocomplete':'off'})

    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscriber.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
