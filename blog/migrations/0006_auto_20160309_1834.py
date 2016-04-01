# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_caosblogpage_disclaimer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caosblogpage',
            name='footer',
        ),
        migrations.AddField(
            model_name='caosblogpage',
            name='footernote',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Footnote', null=True),
        ),
    ]
