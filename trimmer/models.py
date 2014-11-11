import re

from django.db import models
from django.core.cache import get_cache
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


cache = get_cache('default')


class URLManager(models.Manager):
    def create_url(self, url):
        """
        Match items for the given url, if none matches pick random one
        from the list, if all the words are used must reuse existing one,
        must reuse in order ascending of when they were used first.
        If given url already have tinyurl assigned to it, will return
        existing.
        :param url: type URL
        :return: TinyURL object
        """
        try:
            item = self.get(url=url)
        except ObjectDoesNotExist:
            pass
        else:
            return item

        all_words = list(self.filter(Q(url=None) | Q(url=""))
                         .values_list('word', flat=True))

        if not all_words:
            url_obj = self.order_by('updated')[0]
            # return url_obj.word
        else:
            all_words.sort(key=len, reverse=True)
            cached_regex = '|'.join(all_words)
            regex = re.compile(cached_regex)
            word = url.split("/")[-2]
            match = regex.match(word)

            if match:
                group = match.group()
            else:
                group = all_words.pop()

            url_obj = self.get(word=group)

        url_obj.url = url
        url_obj.save()

        return url_obj


class TinyURL(models.Model):
    word = models.CharField(max_length=200, unique=True)
    added = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField()

    objects = URLManager()
