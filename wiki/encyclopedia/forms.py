from django import forms

class NewPage(forms.Form):
    title = forms.CharField(
        label="Page Title", widget=forms.TextInput(attrs={"style": "width: 300px", "class": "form-control"})
        )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": "30", "class": "form-control"})
        )