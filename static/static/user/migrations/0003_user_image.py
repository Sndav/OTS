# Generated by Django 2.1.4 on 2018-12-14 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181214_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y%m'),
        ),
    ]
