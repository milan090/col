from django.shortcuts import render
from .models import Course, UserCourses, CourseLesson
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(req):
    allcourses = Course.objects.all()
    usercourses = []
    if req.user.is_authenticated:
        usercourses = [i.course for i in UserCourses.objects.filter(user=req.user)]

        
    return render(req, 'courses.html',{
        'allcourses':allcourses,
        'usercourses':usercourses,
    })

@login_required
def usercourses(req):
    user_courses = UserCourses.objects.filter(user=req.user)
    if len(user_courses) == 0:
        print('No courses')
        user_courses=None
    return render(req, 'user_courses.html',{
        'user_courses':user_courses,
    })



@login_required
def addcourse(req):
    if req.method == 'GET':
        user = req.user
        course_to_add_name = req.GET.get('coursename')
        print(user_has_course(user,course_to_add_name))
        if user_has_course(user,course_to_add_name):
            return HttpResponse("Course not added"+' '+ course_to_add_name)
        elif user_has_course(user,course_to_add_name) == None:
            return HttpResponse('No such course named' + ' ' + course_to_add_name)
        else:
            course = Course.objects.get(course_name=course_to_add_name)
            usercourse = UserCourses(user=user, course=course)
            usercourse.save()
            return HttpResponseRedirect(reverse('user_courses'))

@login_required
def remove_course(req):
    if req.method == 'GET':
        user = req.user
        course_to_remove_name = req.GET.get('coursename')
        print(user_has_course(user,course_to_remove_name))
        if user_has_course(user,course_to_remove_name):
            course = Course.objects.get(course_name=course_to_remove_name)
            usercourse = UserCourses.objects.get(course=course, user=user)
            usercourse.delete()
            return HttpResponseRedirect(reverse('user_courses'))

        elif user_has_course(user,course_to_remove_name) == None:
            return HttpResponse('No such course named' + ' ' + course_to_remove_name)
        else:
            return HttpResponse("Course not removed"+' '+ course_to_remove_name)
        
def user_has_course(user,course_name):
    all_user_courses = [i.course for i in UserCourses.objects.filter(user=user)]
    try:
        course = Course.objects.get(course_name=course_name)
    except Course.DoesNotExist:
        course = None
    if course==None:
        return course
    elif course in all_user_courses:
        return True
    else:
        return False


def python_beginners_course(req):
    course = Course.objects.get(course_url='python-beginners-course')
    course_lessons = CourseLesson.objects.filter(course=course)
    print(course_lessons)
    return render(req, course.course_url+'/coursepage.html', {
        'course_lessons':course_lessons,
    })


def web_development(req):
    return HttpResponse('Under development')

def lesson_urls(lesson):
    course = lesson.course
    def lesson_view(req):
        print(str(lesson.lesson_url))
        return render(req, lesson.course.course_url+'/'+lesson.lesson_url+'.html',{
            'lesson':lesson,
        })
    return lesson_view