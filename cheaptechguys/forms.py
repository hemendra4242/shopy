from django import forms
from .models import contact_us, Account, Comment, wishlist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

class Commentform(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 5}))
    class Meta:
        model = Comment
        fields = ['comment']

class Profileform(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'profile_image']


class wishlistform(forms.ModelForm):
    class Meta:
        model = wishlist
        fields = '__all__'


