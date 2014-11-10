from django import forms

from .models import TinyURL


class URLForm(forms.Form):
    url = forms.CharField()
    word = forms.CharField(widget=forms.HiddenInput(),
                            initial="nothing")

    def clean_word(self):
        return TinyURL.objects.suggest_url(self.cleaned_data["url"])

    def save(self):
        url_obj = TinyURL.objects.get(word=self.cleaned_data["word"])
        url_obj.url = self.cleaned_data["url"]
        url_obj.save()
        return url_obj