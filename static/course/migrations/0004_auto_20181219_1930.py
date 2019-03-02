# Generated by Django 2.1.4 on 2018-12-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_courseresource_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseresource',
            name='download',
            field=models.FileField(default='resource/default.doc', upload_to='resource/%Y/%m/%d', verbose_name='资源文件'),
        ),
        migrations.AlterField(
            model_name='lessondetail',
            name='detail',
            field=models.TextField(default='', verbose_name='课程内容'),
        ),
    ]