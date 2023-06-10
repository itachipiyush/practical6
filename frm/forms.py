# forms.py
from django import forms

class MyForm(forms.Form):
    Your_member_id = forms.CharField(max_length=100)
    Your_email_id = forms.EmailField()
    Your_course = forms.CharField(max_length=100)
    staff = forms.BooleanField(required=False, widget=forms.CheckboxInput)
