from django import forms

class Contact(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter your message", "style":"width: 500px;", "class":"form-control"}))    