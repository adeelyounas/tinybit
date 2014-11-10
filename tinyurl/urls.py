from django.conf.urls import patterns, url

from trimmer.views import TrimmerView, LinkView


urlpatterns = patterns(
    '',
    url(r'^url/trimmer/', TrimmerView.as_view()),
    url(r'^(?P<word>[\w\d]+)$', LinkView.as_view())
)
