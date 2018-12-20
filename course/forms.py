from django import forms
from captcha.fields import CaptchaField
from .models import *


class CreateCourse(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Course
        fields = ["name", "desc", "detail", "degree", "required_knowledge"]


class AddLesson(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Lesson
        fields = ["course", "name"]
