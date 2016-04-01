# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160309_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caosblogpage',
            name='footer',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Footer', blank=True, null=True),
        ),
    ]
