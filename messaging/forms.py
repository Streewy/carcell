from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Message

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.'
    )

    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.'
    )

    plate_number = forms.CharField(
        max_length=15,
        required=False,
        help_text='Optional.'
    )

    email = forms.CharField(
        required=True,
        label='E-mail',
        max_length=32,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'plate_number')

class MessageSendingForm(forms.Form):
    sender = forms.CharField(
        max_length=254,
        required=True,
    )

    plate = forms.CharField(
        max_length=15,
        required=True,
        help_text='Receiver\'s plate number.'
    )

    content = forms.CharField(
        max_length=254,
        required=True,
        help_text='Message to be sent.'
    )

    class Meta:
        model = Message
        fields = ('sender', 'plate', 'content',)
