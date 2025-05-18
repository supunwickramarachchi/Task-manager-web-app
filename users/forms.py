from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your username',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your email',
        })
        self.fields['age'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your age',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Confirm your password',
        })
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your username',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your email',
        })
        self.fields['age'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your age',
        })
        
class TailwindLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your username',
        })

        self.fields['password'].widget.attrs.update({
            'class': 'w-full p-2 border border-gray-300 rounded',
            'placeholder': 'Enter your password',
        })