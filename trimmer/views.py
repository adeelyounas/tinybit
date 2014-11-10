from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from .forms import URLForm
from .models import TinyURL


class TrimmerView(View):
    template_name = 'trimmer.html'
    form_class = URLForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={})
        template_dict = {
            'form': form
        }

        word = request.GET.get("word")
        if word:
            template_dict["tiny_url"] = "http://%(host)s:%(port)s/%(word)s" % {
                "host": settings.HOST,
                "port": settings.PORT,
                "word": word
            }
            template_dict["url"] = request.GET.get('url')

        return render(request, self.template_name, template_dict)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            url_obj = form.save()

            return HttpResponseRedirect('/url/trimmer/?word=%s&url=%s'
                                        % (url_obj.word, url_obj.url))

        return render(request, self.template_name, {'form': form})


class LinkView(View):

    def get(self, request, word, *args, **kwargs):
        try:
            url_obj = TinyURL.objects.get(word=word.lower())
        except ObjectDoesNotExist:
            return HttpResponse("Requested URL Not Found")
        return HttpResponseRedirect(url_obj.url)