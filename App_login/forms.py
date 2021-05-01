from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from App_login.models import UserProfile
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email =forms.EmailField(label="Email Address",required=True)
    class Meta:
        model=User
        fields=('username','email','password1','password2')


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model=User
        fields=('email','first_name','last_name','password')
        
        
class PictureChangeForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_pic',]