from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=80, unique=True)
    course_discription = models.CharField(max_length=800)
    course_url = models.CharField(max_length=30)

    def __str__(self):
        return self.course_url

class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    lesson_name = models.CharField(max_length=50, blank=True)
    lesson_url = models.CharField(max_length=30)

    def __str__(self):
        return self.lesson_name

class UserCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_progress = models.IntegerField(default=0)

    def __str__(self):
        return self.course.course_url + ' ' + self.user.username