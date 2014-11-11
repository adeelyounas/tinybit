from django import forms

from .models import TinyURL


class URLForm(forms.Form):
    url = forms.CharField()
    word = forms.CharField(widget=forms.HiddenInput(), initial="nothing")

    def save(self):
        return TinyURL.objects.create_url(url=self.cleaned_data["url"])