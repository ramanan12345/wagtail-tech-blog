# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160309_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caosblogpage',
            old_name='footernote',
            new_name='footnote',
        ),
    ]
