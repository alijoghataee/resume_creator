# Generated by Django 4.1.5 on 2023-01-15 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='project',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='social_media',
        ),
    ]
