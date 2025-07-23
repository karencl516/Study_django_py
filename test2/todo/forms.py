from django import forms

class AddTasks(forms.Form):
    task = forms.CharField()