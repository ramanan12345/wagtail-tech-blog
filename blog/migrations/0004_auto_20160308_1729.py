# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160301_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caosblogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('date', wagtail.wagtailcore.blocks.DateBlock()), ('codeblock', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'Python'), ('javascript', 'Javascript'), ('json', 'JSON'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS'), ('scss', 'SCSS'), ('yaml', 'YAML'), ('mysql', 'MySQL')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))))),
        ),
    ]
