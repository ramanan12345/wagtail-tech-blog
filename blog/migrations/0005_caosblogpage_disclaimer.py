# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160308_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='caosblogpage',
            name='disclaimer',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Disclaimer', null=True, blank=True),
        ),
    ]
