from django.views import View
from django.shortcuts import render, HttpResponseRedirect
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from .forms import *
from .models import *


# Course
class AddCourseView(View):
    def get(self, request):
        course_form = CourseFrom()
        hashkey = CaptchaStore.generate_key()
        imageURL = captcha_image_url(hashkey)

        return render(request, 'course/addcourse.html', {
            'form': course_form,
            'hashkey': hashkey,
            'image_url': imageURL

        })

    def post(self, request):
        course_form = CourseFrom(request.POST)
        if course_form.is_valid():
            ret = course_form.save()
            return HttpResponseRedirect('/course/{0}/view'.format(ret.pk))
        else:
            hashkey = CaptchaStore.generate_key()
            imageURL = captcha_image_url(hashkey)
            return render(request, 'course/addcourse.html', {
                'form': course_form,
                'hashkey': hashkey,
                'image_url': imageURL

            })


class EditCourseView(View):
    def get(self, request, course_id):
        course_form = CourseFrom(instance=Course.objects.get(id=course_id))
        return render(request, 'course/editcourse.html', {'form': course_form})

    def post(self, request, course_id):
        course_form = CourseFrom(request.POST, instance=Course.objects.get(id=course_id))
        if course_form.is_valid():
            course_form.save()
            return HttpResponseRedirect('/course/all')
        else:
            return render(request, 'course/editcourse.html', {'form': course_form})


class ViewCourseView(View):
    def get(self, request, course_id):
        course_form = Course.objects.get(id=course_id)
        return render(request, 'course/viewcourse.html', {'form': course_form})


class ViewAllCourseView(View):
    def get(self, request):
        form = Course.objects.filter(teacher=request.user.id)
        return render(request, 'course/viewallcourse.html', {'form': form})


class ViewDeleteCourseView(View):
    def get(self, request, course_id):
        model = Course.objects.get(id=course_id)
        form = Course.delete(model)
        return HttpResponseRedirect('/course/all')


# Lesson
class AddLessonView(View):
    def get(self, request, course_id):
        lesson_form = LessonForm()
        lesson_form.fields['course'].queryset = Course.objects.filter(pk=course_id)
        return render(request, 'course/lesson/addlesson.html', {'form': lesson_form,'course_id':course_id})

    def post(self, request, course_id):
        lesson_form = LessonForm(request.POST)
        if lesson_form.is_valid():
            ret = lesson_form.save()
            return HttpResponseRedirect('/course/{0}/lesson'.format(ret.course.pk, ret.pk))
        else:
            return render(request, 'course/lesson/addlesson.html', {'form': lesson_form})


class EditLessonView(View):
    def get(self, request, course_id, lesson_id):
        lesson_form = LessonForm(instance=Lesson.objects.get(pk=lesson_id))
        lesson_form.fields['course'].queryset = Course.objects.filter(pk=course_id)
        return render(request, 'course/lesson/editlesson.html', {'form': lesson_form})

    def post(self, request, course_id, lesson_id):
        lesson_form = LessonForm(request.POST, instance=Lesson.objects.get(pk=lesson_id))
        if lesson_form.is_valid():
            ret = lesson_form.save()
            return HttpResponseRedirect('/course/{0}/lesson'.format(ret.course.pk, ret.pk))
        else:
            return render(request, 'course/lesson/editlesson.html', {'form': lesson_form})


class ViewLessonView(View):
    def get(self, request, course_id, lesson_id):
        lesson_form = Lesson.objects.get(id=lesson_id).__dict__
        return render(request, 'course/lesson/viewlesson.html', {'form': lesson_form})


class ViewAllLessonView(View):
    def get(self, request, course_id):
        form = Lesson.objects.filter(course_id=course_id)
        return render(request, 'course/lesson/viewalllesson.html', {'form': form})


class DeleteLessonView(View):
    def get(self, request, course_id, lesson_id):
        form = Lesson.objects.get(id=lesson_id)
        Lesson.delete(form)
        return HttpResponseRedirect('/course/{0}/lesson'.format(course_id))


# LessonDetail
class AddLessonDetail(View):
    def get(self, request, course_id, lesson_id):
        lesson_form = LessonDetailForm()
        lesson_form.fields['lesson'].queryset = Lesson.objects.filter(pk=lesson_id)
        return render(request, 'course/lesson/detail/addlessondetail.html', {'form': lesson_form,'lesson_id':lesson_id})

    def post(self, request, course_id, lesson_id):
        lesson_form = LessonDetailForm(request.POST)
        if lesson_form.is_valid():
            ret = lesson_form.save()
            print(ret)
            return HttpResponseRedirect('/course/{0}/lesson/{1}/detail'.format(
                ret.lesson.course.pk,
                ret.lesson.pk,
                ret.pk
            ))
        else:
            return render(request, 'course/lesson/detail/addlessondetail.html', {'form': lesson_form})


class EditLessonDetail(View):
    def get(self, request, course_id, lesson_id, detail_id):
        lesson_form = LessonDetailForm(instance=LessonDetail.objects.get(pk=detail_id))
        lesson_form.fields['lesson'].queryset = Lesson.objects.filter(pk=lesson_id)
        return render(request, 'course/lesson/detail/editlessondetail.html', {'form': lesson_form,'lesson_id':lesson_id})

    def post(self, request, course_id, lesson_id, detail_id):
        lesson_form = LessonDetailForm(request.POST, instance=LessonDetail.objects.get(pk=detail_id))
        if lesson_form.is_valid():
            ret = lesson_form.save()
            return HttpResponseRedirect('/course/{0}/lesson/{1}/detail'.format(
                ret.lesson.course.pk,
                ret.lesson.pk,
                ret.pk
            ))
        else:
            return render(request, 'course/lesson/detail/editlessondetail.html', {'form': lesson_form})


class ViewLessonDetail(View):
    def get(self, request, course_id, lesson_id, detail_id):
        lesson_form = LessonDetail.objects.get(id=detail_id)
        return render(request, 'course/lesson/detail/viewlessondetail.html', {'form': lesson_form})


class ViewAllLessonDetail(View):
    def get(self, request, course_id, lesson_id):
        lesson_form = LessonDetail.objects.filter(lesson_id=lesson_id)
        return render(request, 'course/lesson/detail/viewalldetail.html', {'form': lesson_form})


class DeleteLessonDetail(View):
    def get(self, request, course_id, lesson_id, detail_id):
        detail_form = LessonDetail.objects.get(id=detail_id)
        LessonDetail.delete(detail_form)
        return HttpResponseRedirect('/course/{0}/lesson/{1}/detail'.format(
            course_id,
            lesson_id,
            detail_id
        ))


# LessonRecourse
class AddLessonResource(View):
    def get(self, request, course_id, lesson_id):
        lesson_form = LessonResourceForm()
        lesson_form.fields['lesson'].queryset = Lesson.objects.filter(pk=lesson_id)
        return render(request, 'course/lesson/resource/addlessonresource.html', {'form': lesson_form})

    def post(self, request, course_id, lesson_id):
        lesson_form = LessonResourceForm(request.POST, request.FILES)
        if lesson_form.is_valid():
            ret = lesson_form.save()
            print(ret)
            return HttpResponseRedirect('/course/{0}/lesson/{1}/resource/{2}/view'.format(
                ret.lesson.course.pk,
                ret.lesson.pk,
                ret.pk
            ))
        else:
            return render(request, 'course/lesson/resource/addlessonresource.html', {'form': lesson_form})


class EditLessonResource(View):
    def get(self, request, course_id, lesson_id, resource_id):
        lesson_form = LessonResourceForm(instance=LessonResource.objects.get(pk=resource_id))
        lesson_form.fields['lesson'].queryset = Lesson.objects.filter(pk=lesson_id)
        return render(request, 'course/lesson/resource/editlessonresource.html', {'form': lesson_form})

    def post(self, request, course_id, lesson_id, resource_id):
        lesson_form = LessonResourceForm(request.POST, request.FILES, instance=LessonResource.objects.get(pk=resource_id))
        if lesson_form.is_valid():
            ret = lesson_form.save()
            return HttpResponseRedirect('/course/{0}/lesson/{1}/resource/{2}/view'.format(
                ret.lesson.course.pk,
                ret.lesson.pk,
                ret.pk
            ))
        else:
            return render(request, 'course/lesson/resource/editlessonresource.html', {'form': lesson_form})


class ViewLessonResource(View):
    def get(self, request, course_id, lesson_id, resource_id):
        lesson_form = LessonResource.objects.get(id=resource_id).__dict__
        return render(request, 'course/lesson/resource/viewlessonresource.html', {'form': lesson_form})


# Note
class AddLessonNote(View):
    def get(self, request, course_id, lesson_id):
        lesson_form = LessonNoteForm()
        lesson_form.fields['lesson'].queryset = Lesson.objects.filter(pk=lesson_id)
        return render(request, 'course/lesson/note/addlessonnote.html', {'form': lesson_form})

    def post(self, request, course_id, lesson_id):
        lesson_form = LessonNoteForm(request.POST)
        if lesson_form.is_valid():
            ret = lesson_form.save()
            print(ret)
            return HttpResponseRedirect('/course/{0}/lesson/{1}/note/{2}/view'.format(
                ret.lesson.course.pk,
                ret.lesson.pk,
                ret.pk
            ))
        else:
            return render(request, 'course/lesson/note/addlessonnote.html', {'form': lesson_form})


class EditLessonNote(View):
    def get(self, request, course_id, lesson_id, note_id):
        lesson_form = LessonNoteForm(instance=LessonNote.objects.get(pk=note_id))
        lesson_form.fields['lesson'].queryset = Lesson.objects.filter(pk=lesson_id)
        return render(request, 'course/lesson/note/editlessonnote.html', {'form': lesson_form})

    def post(self, request, course_id, lesson_id, note_id):
        lesson_form = LessonNoteForm(request.POST, instance=LessonNote.objects.get(pk=note_id))
        if lesson_form.is_valid():
            ret = lesson_form.save()
            return HttpResponseRedirect('/course/{0}/lesson/{1}/note/{2}/view'.format(
                ret.lesson.course.pk,
                ret.lesson.pk,
                ret.pk
            ))
        else:
            return render(request, 'course/lesson/note/editlessonnote.html', {'form': lesson_form})


class ViewLessonNote(View):
    def get(self, request, course_id, lesson_id, note_id):
        lesson_form = LessonNote.objects.get(id=note_id).__dict__
        return render(request, 'course/lesson/note/viewlessonnote.html', {'form': lesson_form})
