from django import forms

class TicketForm(forms.Form):
    pass

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)