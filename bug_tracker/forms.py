from django import forms

class TicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class StatusForm(forms.Form):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    ]
    status_change = forms.ChoiceField(
        choices = STATUS_CHOICES
    )