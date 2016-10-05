from django import forms

class AdminForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    imap_hostname = forms.CharField(label='IMAP hostname',max_length=100)
    smtp_hostname = forms.CharField(label='SMTP hostname',max_length=100)
