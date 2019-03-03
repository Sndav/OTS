from django import forms
from captcha.fields import CaptchaField
from .models import *


class CourseFrom(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Course
        fields = ["name", "desc", "detail", "degree", "required_knowledge"]


class LessonForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Lesson
        fields = ["course", "name"]


class LessonDetailForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = LessonDetail
        fields = ["lesson", "detail"]


class LessonResourceForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = LessonResource
        fields = ["lesson", "name", "download"]


class LessonNoteForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = LessonNote
        fields = ["lesson", "user", "note"]
