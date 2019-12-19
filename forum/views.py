from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Answer, Question
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(req):
    return render(req, 'forum.html')

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
