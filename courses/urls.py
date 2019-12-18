from django.urls import path
from . import views
from .models import CourseLesson

urlpatterns = [
    path('', views.index, name='courses'),
    path('my-courses/', views.usercourses, name='user_courses'),
    path('add-course', views.addcourse, name='add_course'),
    path('remove-course', views.remove_course, name='remove_course'),
    path('python-beginners-course/', views.python_beginners_course, name='python-beginners-course'),
    path('web-development-easy', views.web_development_easy, name='web-development-easy'),

]

for lesson in CourseLesson.objects.all():
    url = lesson.course.course_url +'/'+lesson.lesson_url
    urlpatterns.append(path(url, views.lesson_urls(lesson), name=lesson.course.course_url +'-'+ lesson.lesson_url))

