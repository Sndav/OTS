# Generated by Django 2.1.4 on 2018-12-14 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessondetail',
            options={'verbose_name': '章节细节', 'verbose_name_plural': '章节细节'},
        ),
        migrations.AlterModelOptions(
            name='lessonnode',
            options={'verbose_name': '笔记内容', 'verbose_name_plural': '笔记内容'},
        ),
    ]