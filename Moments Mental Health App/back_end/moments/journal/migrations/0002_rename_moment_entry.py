# Generated by Django 3.2.1 on 2021-05-04 05:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Moment',
            new_name='Entry',
        ),
    ]
