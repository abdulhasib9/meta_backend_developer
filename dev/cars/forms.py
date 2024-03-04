from django import forms

class review_form(forms.Form):
    name = forms.CharField(label='Name: ',)