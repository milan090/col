from django.shortcuts import render
from .models import UserProfileInfo
from .forms import UserProfileInfoForm, UserForm

#
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .userverfiy import fn_generate_token
from django.core.mail import send_mail


# Create your views here.
def index(req):
    if req.user.is_authenticated:
        userProfile = UserProfileInfo.objects.filter(user=req.user)[0]
        try:
            img = userProfile.profile_pic
        except:
            img = None
        print(img)
        return render(req, 'index.html', {
            'profile_pic': img,
        })
    else:
        return render(req, 'index.html')

def register(req):
    registered = False

    if req.method == 'POST':
        user_form = UserForm(data=req.POST)
        profile_form = UserProfileInfoForm(data=req.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            if 'profile_pic' in req.FILES:
                user_profile.profile_pic = req.FILES['profile_pic']
            user_profile.save()
            registered = True

            try:
                send_mail(
                    'Email Confirmation - COL',
                    'Click the link to confirm \n {}'.format(fn_generate_token(user.id)),
                    'milanmuhammed1@gmail.com',
                    [req.POST['email']],
                    fail_silently=False,
                )
            except:
                pass
            return HttpResponseRedirect(reverse('user_login'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(req, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

def user_login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(req, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('User is not Active')
        else:
            return HttpResponse('Inavlid login Credential. Go back to try again')
    else:
        return render(req, 'login.html')


@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(req):
    return HttpResponse('You are special')

