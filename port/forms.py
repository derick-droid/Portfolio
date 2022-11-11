from django import forms

class Contact(forms.Form):
    name = forms.CharField(max_length=200)
    email  = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)    