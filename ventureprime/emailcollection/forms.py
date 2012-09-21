from django import forms

class EmailCollectionForm(forms.Form):
    email = forms.EmailField(max_length=100)
    #Takes values 'Venture', 'Primer', or 'Both'
    user_type = forms.CharField(max_length=30,label='User Type (Venture, Primer, or Both)')