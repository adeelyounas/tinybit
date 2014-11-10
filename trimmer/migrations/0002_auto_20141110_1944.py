# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trimmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TinyURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('word', models.CharField(unique=True, max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='TinyURLs',
        ),
        migrations.DeleteModel(
            name='Words',
        ),
    ]
