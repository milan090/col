from django.contrib import admin
from .models import Course, CourseLesson, UserCourses

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseLesson)
admin.site.register(UserCourses)