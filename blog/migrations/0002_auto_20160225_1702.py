# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caosblogpage',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('Python', 'Python'), ('CSS3', 'CSS3'), ('HTML5', 'HTML5'), ('Philosophy of Tech', 'Philosophy of Tech'), ('Javascript', 'Javascript'), ('ReactJS', 'ReactJS'), ('DevOps', 'DevOps'), ('UI, UX', 'UI, UX'), ('Python, Django', 'Python, Django')], default=None, max_length=40),
        ),
    ]
