# Generated by Django 3.2 on 2021-05-02 19:51

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(default='defaults/profile-placeholder.jpg', upload_to=accounts.models.profile_photo_upload),
        ),
    ]