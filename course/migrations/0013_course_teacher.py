# Generated by Django 2.1.4 on 2019-03-04 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20190303_2048'),
        ('course', '0012_auto_20181221_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='讲师'),
            preserve_default=False,
        ),
    ]
