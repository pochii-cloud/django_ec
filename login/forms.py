from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from login.models import Contact, Product, Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['username','email','phone','message']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','Category','description','image']

class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','image','body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
