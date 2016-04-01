# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
        ('wagtailimages', '0008_image_created_at_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaosAboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', primary_key=True, parent_link=True, auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('about_head_img', models.ForeignKey(null=True, related_name='+', blank=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('bio', models.CharField(max_length=200)),
                ('profile_img', models.ForeignKey(null=True, related_name='+', blank=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileIndex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('page', modelcluster.fields.ParentalKey(to='about.CaosAboutPage', related_name='CaosProfiles')),
                ('profile', models.ForeignKey(to='about.Profile', related_name='+')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
