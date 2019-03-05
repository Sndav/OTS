from django.urls import path
from . import views

urlpatterns = [
    # 课程 /course/add
    #     /course/<id>/(edit,view,delete)
    #     /course/all/
    path(
        'add',
        views.AddCourseView.as_view(),
        name='添加课程'),
    path(
        '<int:course_id>/edit/',
        views.EditCourseView.as_view(),
        name='编辑课程'),
    path(
        '<int:course_id>/view/',
        views.ViewCourseView.as_view(),
        name='查看课程'),
    path(
        'all',
        views.ViewAllCourseView.as_view(),
        name='查看所有课程'
    ),
    path(
        '',
        views.ViewAllCourseView.as_view(),
        name='查看所有课程'
    ),
    path(
        '<int:course_id>/delete/',
        views.ViewDeleteCourseView.as_view(),
        name='删除课程'
    ),
    # 章节 /course/<id>/lesson/add
    #     /course/<id>/lesson
    #     /course/<id>/lesson/<id>/(delete,edit,view)
    path(
        '<int:course_id>/lesson/add',
        views.AddLessonView.as_view(),
        name='添加章节'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/edit',
        views.EditLessonView.as_view(),
        name='更改章节'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/view',
        views.ViewLessonView.as_view(),
        name='查看章节'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/delete',
        views.DeleteLessonView.as_view(),
        name='删除章节'),
    path(
        '<int:course_id>/lesson/',
        views.ViewAllLessonView.as_view(),
        name="查看所有章节"
    ),


    # 章节细节 /course/<id>/lesson/<id>/detail/add
    #        /course/<id>/lesson/<id>/detail/<id>/(edit,view)
    path(
        '<int:course_id>/lesson/<int:lesson_id>/detail/add',
        views.AddLessonDetail.as_view(),
        name='添加章节细节'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/detail/<int:detail_id>/edit/',
        views.EditLessonDetail.as_view(),
        name='更改章节细节'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/detail/<int:detail_id>/view/',
        views.ViewLessonDetail.as_view(),
        name='查看章节细节'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/detail',
        views.ViewAllLessonDetail.as_view(),
        name='查看所有章节细节'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/detail/<int:detail_id>/delete',
        views.DeleteLessonDetail.as_view(),
        name='删除章节细节'),
    # 章节资源 /course/<id>/lesson/<id>/resource/add
    #        /course/<id>/lesson/<id>/resource/<id>/(edit,view)
    path(
        '<int:course_id>/lesson/<int:lesson_id>/resource/add/',
        views.AddLessonResource.as_view(),
        name='添加章节资源'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/resource/<int:resource_id>/edit/',
        views.EditLessonResource.as_view(),
        name='编辑章节资源'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/resource/<int:resource_id>/view',
        views.ViewLessonResource.as_view(),
        name='查看章节资源'),

    # 笔记 /course/<id>/lesson/<id>/note/add
    #     /course/<id>/lesson/<id>/note/<id>/(edit,view)
    path(
        '<int:course_id>/lesson/note/add',
        views.AddLessonNote.as_view(),
        name='添加笔记'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/note/<int:note_id>/edit/',
        views.EditLessonNote.as_view(),
        name='编辑笔记'),
    path(
        '<int:course_id>/lesson/<int:lesson_id>/note/<int:note_id>/view/',
        views.ViewLessonNote.as_view(),
        name='查看笔记'),
]
