from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task, AppUser

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']

class AppUserForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'password1', 'password2' ,'bio', 'position']
        widgets = {
            'password': forms.PasswordInput(),
        }