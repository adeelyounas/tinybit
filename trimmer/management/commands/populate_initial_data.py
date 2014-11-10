import re

from django.core.management.base import BaseCommand
from trimmer.models import TinyURL


class Command(BaseCommand):
    help = 'This will wipe and repopulate the database with words'

    def handle(self, *args, **options):
        TinyURL.objects.all().delete()
        regex = re.compile(r'^[a-zA-Z0-9]+$')
        with open('./static_files/words.txt', "r+") as f:
            for word in f:
                word = word.strip("\n")
                if regex.match(word):
                    TinyURL.objects.get_or_create(word=word.lower())
