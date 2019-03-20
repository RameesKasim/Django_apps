from django import forms


class HelpRequestForm(forms.Form):
    name = forms.CharField(max_length=50)
    house = forms.CharField(max_length=50)
    place = forms.CharField(max_length=50)
    contact = forms.NumberInput()
    type = forms.CharField(max_length=50)
    help_needed = forms.CharField(max_length=50)
    letter = forms.CharField(max_length=100)
