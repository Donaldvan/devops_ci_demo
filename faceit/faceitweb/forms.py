from django import forms

class UserForm(form.Form):
    full_name = forms.CharField(label="Your Name", max_length=70)
