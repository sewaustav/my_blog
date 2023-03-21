from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput, PasswordInput, CharField, EmailField
from .models import *


class CreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text']

        widgets = {
            'title': TextInput(attrs={'class': 'input-text','id': 'title-create', 'placeholder': 'Title'}),
            'text': Textarea(attrs={'class': 'input-text', 'id': 'text-create', 'placeholder': 'Text'}),
        }