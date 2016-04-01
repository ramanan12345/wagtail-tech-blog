# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160225_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caosblogpage',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(default=None, choices=[('Django', 'Django'), ('Python', 'Python'), ('CSS3', 'CSS3'), ('HTML5', 'HTML5'), ('Philosophy of Tech', 'Philosophy of Tech'), ('Tech Trends', 'Tech Trends'), ('Javascript', 'Javascript'), ('ReactJS', 'ReactJS'), ('DevOps', 'DevOps'), ('UI, UX', 'UI, UX'), ('Python, Django', 'Python, Django')], max_length=40),
        ),
    ]
