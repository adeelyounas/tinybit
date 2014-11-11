from django.test import TestCase
from trimmer.models import TinyURL


class TinyURLTestCase(TestCase):
    def setUp(self):
        self.words = ["tinyurl", "tinybit", "test", "bit"]
        for word in self.words:
            TinyURL.objects.create(word=word)

    def test_generate_tiny_url(self):
        """Test generating tiny url when empty words available,
        reuse when all the available words are used"""
        for word in self.words:
            url = "http://www.web.com/%s/" % word
            url_obj = TinyURL.objects.create_url(url=url)

            self.assertEqual(url_obj.word, word)

        # Test generating tiny url when all the words are used,
        # should pick/reuse word that was used first
        first_used = TinyURL.objects.order_by('updated')[0]

        reuse_word = TinyURL.objects.create_url(
            url="http://www.web.com/justtesting/")

        self.assertEqual(reuse_word.word, first_used.word)
