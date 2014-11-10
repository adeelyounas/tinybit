import re

from django.db import models
from django.core.cache import get_cache
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


cache = get_cache('default')


class URLManager(models.Manager):
    def suggest_url(self, url):
        """
        Match items for the given url, if none matches pick random one
        from the list.
        :param url: type URL
        :return: group matched the url or random one
        """
        try:
            item = self.get(url=url)
        except ObjectDoesNotExist:
            pass
        else:
            return item.word

        all_words = list(self.filter(Q(url=None) | Q(url=""))
                         .values_list('word', flat=True))

        all_words.sort(key=len, reverse=True)
        cached_regex = '|'.join(all_words)
        regex = re.compile(cached_regex)
        word = url.split("/")[-2]
        match = regex.match(word)

        if match:
            group = match.group()
        else:
            group = all_words.pop()

        return group


class TinyURL(models.Model):
    word = models.CharField(max_length=200, unique=True)
    added = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField()

    objects = URLManager()
