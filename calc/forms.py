from django import forms

class ExprForm(forms.Form):
    expression = forms.CharField(max_length=500)