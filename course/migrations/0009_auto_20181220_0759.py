# Generated by Django 2.1.4 on 2018-12-19 23:59

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20181220_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessondetail',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程内容'),
        ),
    ]
