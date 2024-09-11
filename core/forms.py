from django import forms
from django.contrib.auth.forms import UserCreationForm




class user_signup(forms.ModelForm):
    class Meta:
        model=UserCreationForm()
        fields=['username','first_name','last_name','password1','password2']
        widgets={'password2':forms.PasswordInput(attrs={'label':'Confirm Password'})}