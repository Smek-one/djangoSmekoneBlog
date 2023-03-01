from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Email", required=True)
    firstname = forms.CharField(label="Prénom", max_length=20)
    lastname = forms.CharField(label="Nom", max_length=20)
    subject = forms.CharField(label="Sujet", required=True)
    message = forms.CharField(label="Votre message", widget=forms.Textarea, required=True)
