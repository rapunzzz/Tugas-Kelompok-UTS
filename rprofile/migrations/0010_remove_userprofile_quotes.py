# Generated by Django 4.2.4 on 2023-10-28 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rprofile', '0009_remove_userprofile_quotes_userprofile_quotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='quotes',
        ),
    ]
