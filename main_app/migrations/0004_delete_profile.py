# Generated by Django 4.1 on 2023-11-21 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_lesson_secondary_vimeo_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
