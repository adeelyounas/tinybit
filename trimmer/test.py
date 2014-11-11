from django.test import TestCase
from trimmer.models import TinyURL


class TinyURLTestCase(TestCase):
    def setUp(self):
        self.short_urls = ["tinyurl", "test", "tinybit", "bit"]
        for url in self.short_urls:
            TinyURL.objects.create(word=url)

    def test_generate_tiny_url(self):
        """Test generating tiny url"""
        for url in self.short_urls:
            word = TinyURL.objects.suggest_url(url="http://www.web.com/%s/" % url)
            self.assertEqual(word, url)
