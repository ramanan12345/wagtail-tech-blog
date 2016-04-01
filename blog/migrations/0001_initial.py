# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
        ('wagtailimages', '0008_image_created_at_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaosBlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', primary_key=True, parent_link=True, auto_created=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('date', wagtail.wagtailcore.blocks.DateBlock()), ('codeblock', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'Python'), ('javascript', 'Javascript'), ('json', 'JSON'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
                ('author', models.CharField(max_length=30, choices=[('Chad Whitman', 'Chad Whitman'), ('Bradley Martin', 'Bradley Martin'), ('Steven Turoscy', 'Steven Turoscy'), ('Mikhail Oza', 'Mikhail Oza'), ('CAOS Team', 'CAOS Team')])),
                ('category', multiselectfield.db.fields.MultiSelectField(max_length=40, choices=[('Django', 'Django'), ('Python', 'Python'), ('CSS3', 'CSS3'), ('HTML5', 'HTML5'), ('Philosophy of Tech', 'Philosophy of Tech'), ('DevOps', 'DevOps'), ('UI, UX', 'UI, UX'), ('Python, Django', 'Python, Django')], default=None)),
                ('date', models.DateField(verbose_name='Post date')),
                ('to_read', models.IntegerField(max_length=20, verbose_name='Length To Read')),
                ('footer', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Footer', blank=True)),
                ('blog_head_img', models.ForeignKey(null=True, related_name='+', blank=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
