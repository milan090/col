from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Answer, Question
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(req):
    questions = Question.objects.all().order_by('id').reverse()
    return render(req, 'forum.html', {
        'questions':questions,
    })

@login_required
def ask(req):
    if req.method == 'POST':
        question = req.POST['question']
        description = req.POST['description']
        user = req.user
        q_obj = Question(user=user, title=question, description=description)
        q_obj.save()
        return HttpResponseRedirect(reverse('forum'))
    return render(req, 'ask.html')

def question(req):
    try:
        question_id = req.GET['id']
        question_obj = Question.objects.get(id=question_id)
        answers  = Answer.objects.filter(question=question_obj)
        return render(req, 'question.html', {
            'question': question_obj,
            'answers': answers,
        })
    except :
        return HttpResponse("Http Error")