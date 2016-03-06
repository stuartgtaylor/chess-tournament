# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
from django.conf import settings
import tournament.tournament


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finished', models.BooleanField()),
                ('winner', models.CharField(default=None, max_length=5, null=True, blank=True, choices=[(b'white', b'White'), (b'black', b'Black')])),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True, blank=True)),
            ],
            bases=(tournament.tournament.EloRatingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('rating', models.IntegerField()),
                ('fide_id', models.IntegerField(default=None, null=True, blank=True)),
                ('fide_games', models.IntegerField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RefereeProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('finished', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('side', models.CharField(max_length=5, choices=[(b'white', b'White'), (b'black', b'Black')])),
                ('score', models.FloatField(default=0.0)),
                ('rating_delta', models.FloatField(default=0.0)),
                ('game', models.ForeignKey(to='tournament.Game')),
                ('player', models.ForeignKey(to='tournament.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('finished', models.BooleanField()),
                ('players', models.ManyToManyField(to='tournament.Player')),
                ('referee', models.ForeignKey(to='tournament.RefereeProfile')),
            ],
            bases=(models.Model, tournament.tournament.SwissSystemMixin),
        ),
        migrations.AddField(
            model_name='round',
            name='tournament',
            field=models.ForeignKey(to='tournament.Tournament'),
        ),
        migrations.AddField(
            model_name='game',
            name='black',
            field=models.ForeignKey(related_name='game_set_black', blank=True, to='tournament.Player', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.ForeignKey(to='tournament.Round'),
        ),
        migrations.AddField(
            model_name='game',
            name='white',
            field=models.ForeignKey(related_name='game_set_white', blank=True, to='tournament.Player', null=True),
        ),
    ]
