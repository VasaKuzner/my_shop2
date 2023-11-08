from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Імя')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=15, required=True)
    message = forms.CharField(widget=forms.Textarea, label='Повідомлення')
