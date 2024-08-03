from django import forms # type: ignore

class UploadCSVForm(forms.Form):
    file = forms.FileField()
