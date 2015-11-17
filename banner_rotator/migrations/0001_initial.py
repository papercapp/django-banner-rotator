# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import banner_rotator.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('alt', models.CharField(default='', max_length=255, verbose_name='Image alt', blank=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('url_target', models.CharField(default='', max_length=10, verbose_name='Target', choices=[('_self', 'Current page'), ('_blank', 'Blank page')])),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('max_views', models.IntegerField(default=0, verbose_name='Max views')),
                ('max_clicks', models.IntegerField(default=0, verbose_name='Max clicks')),
                ('clicks', models.IntegerField(default=0, verbose_name='Clicks')),
                ('weight', models.IntegerField(default=5, help_text='A ten will display 10 times more often that a one.', verbose_name='Weight', choices=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]])),
                ('file', models.FileField(upload_to=banner_rotator.models.get_banner_upload_to, verbose_name='File')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_at', models.DateTimeField(default=None, null=True, verbose_name='Start at', blank=True)),
                ('finish_at', models.DateTimeField(default=None, null=True, verbose_name='Finish at', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'campaign',
                'verbose_name_plural': 'campaigns',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Clicked at')),
                ('ip', models.IPAddressField(null=True, blank=True)),
                ('user_agent', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('referrer', models.URLField(null=True, blank=True)),
                ('banner', models.ForeignKey(related_name='click_objects', to='banner_rotator.Banner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('width', models.SmallIntegerField(default=None, null=True, verbose_name='Width', blank=True)),
                ('height', models.SmallIntegerField(default=None, null=True, verbose_name='Height', blank=True)),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('slug',)]),
        ),
        migrations.AddField(
            model_name='click',
            name='place',
            field=models.ForeignKey(related_name='clicks', to='banner_rotator.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='click',
            name='user',
            field=models.ForeignKey(related_name='banner_clicks', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='banner',
            name='campaign',
            field=models.ForeignKey(related_name='banners', default=None, blank=True, to='banner_rotator.Campaign', null=True, verbose_name='Campaign'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='banner',
            name='places',
            field=models.ManyToManyField(related_name='banners', verbose_name='Place', to='banner_rotator.Place', db_index=True),
            preserve_default=True,
        ),
    ]
