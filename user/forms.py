
from django import forms
#you can customize your validation form
class LoginForm(forms.Form):
    user = forms.CharField(max_length=100,required = False)
    password = forms.CharField(max_length=100,required = False)
    

