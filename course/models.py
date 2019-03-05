from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

import pickle


class Course(models.Model):  # 课程
    DEGREE_CHOICES = (
        ("senior", "初级"),
        ("middle", "中级"),
        ("junior", "高级")
    )
    name = models.CharField("课程名", max_length=100)
    desc = UEditorField("课程描述", imagePath='cimage/', filePath='cfile/', width=0)
    detail = UEditorField("课程详情", imagePath='cimage/', filePath='cfile/', width=0)
    degree = models.CharField('难度', choices=DEGREE_CHOICES, max_length=6)
    students = models.IntegerField("学习人数", default=0)
    fav_nums = models.IntegerField("收藏人数", default=0)
    click_nums = models.IntegerField("点击数", default=0)
    create_time = models.DateTimeField('添加时间', default=datetime.now)
    required_knowledge = UEditorField("预备知识", default=pickle.dumps([{}]))
    update_time = models.DateTimeField('更改时间', auto_now=True)
    teacher = models.ForeignKey('user.User', verbose_name='讲师', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):  # 章节
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField("章节名", max_length=100)
    create_time = models.DateTimeField("添加时间", default=datetime.now)
    update_time = models.DateTimeField('更改时间', auto_now=True)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)


class LessonDetail(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField("课节名", max_length=100)
    detail = UEditorField('课程内容', imagePath='ldimage/', filePath='ldfile/', width=0)
    create_time = models.DateTimeField("添加时间", default=datetime.now)
    update_time = models.DateTimeField('更改时间', auto_now=True)

    class Meta:
        verbose_name = "章节细节"
        verbose_name_plural = verbose_name


class LessonResource(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100)
    download = models.FileField("资源文件", upload_to='resource/%Y/%m/%d')
    create_time = models.DateTimeField("添加时间", default=datetime.now)
    update_time = models.DateTimeField('更改时间', auto_now=True)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name


class LessonNote(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', verbose_name='用户', on_delete=models.CASCADE)
    note = UEditorField('笔记内容', default='', imagePath='lnimage/', filePath='lnfile/', width=0)
    create_time = models.DateTimeField("添加时间", default=datetime.now)
    update_time = models.DateTimeField('更改时间', auto_now=True)

    class Meta:
        verbose_name = "笔记内容"
        verbose_name_plural = verbose_name

