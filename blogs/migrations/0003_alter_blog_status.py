# Generated by Django 5.0.6 on 2024-06-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'published')], default=0),
        ),
    ]
