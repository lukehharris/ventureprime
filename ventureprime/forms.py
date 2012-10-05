from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class CreateUser(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)
    
    USERTYPE_CHOICES = ['Venture','Primer']
    #usertype = forms.ChoiceField(choices=USERTYPE_CHOICES)