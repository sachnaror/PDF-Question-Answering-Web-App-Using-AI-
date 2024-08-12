from django import forms


class PDFUploadForm(forms.Form):
    pdf = forms.FileField()
    question = forms.CharField(max_length=255)
