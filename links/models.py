from django.db import models


class Link(models.Model):
    user = models.ForeignKey('user.User', default=0, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', default=0, verbose_name='课程', on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='总体状态', default=False)
    detail_status = models.ForeignKey('course.LessonDetail', default=0, verbose_name='细节状态', on_delete=models.CASCADE)
