import uuid
from .models import UserToken, PasswordToken
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse

def fn_generate_token(userId):
    if userId > 0:
        exists = UserToken.objects.filter(userId=userId).exists()
        if not exists:
            token = uuid.uuid4()
            link = 'http://col.pythonanywhere.com/ActivateUser?token={}&userId={}'.format(token, userId)
            user_token_obj = UserToken(token=token, userId=userId, link=link)
            user_token_obj.save()
            return link


def fn_verify_token(req):
    try:
        user_id = req.GET['userId']
        verify = UserToken.objects.filter(userId=user_id, token=req.GET['token']).exists()
        if verify:
            user_obj = User.objects.get(id=user_id)
            user_obj.is_active = True
            user_obj.save()
            UserToken.objects.get(userId=user_id).delete()
            try:
                send_mail(
                    'Thank You for registering',
                    'Thank you for registering on CoL. Go and Login right now choose your course.\n https://col.pythonanywhere.com/login',
                    'milanmuhammed1@gmail.com',
                    [str(user_obj.email)],
                    fail_silently=False,
                )
            except:
                return HttpResponse('User activated but didn\'t send thankyou email with email id : ' + str(user_obj.email) )
            return render(req, 'thankyou.html')
        return HttpResponse('invalid token')
    except Exception as identifier:
        pass


def gen_password_token(userId):
    token = uuid.uuid4()
    link = 'http://col.pythonanywhere.com/ChangePassword?token={}&userId={}'.format(token,userId)
    pass_token_obj = PasswordToken(token=token, userId=userId, link=link)
    pass_token_obj.save()
    return link

def forgot_password(req):
    if req.method == 'POST':
        email = req.POST['email']
        userId = User.objects.get(email=email).id

        send_mail(
            'Reset Password',
            'Change your password by clicking the below link. Ignore if not requested by you. \n {}'.format(gen_password_token(userId)),
            'milanmuhammed1@gmail.com',
            [str(email)],
            fail_silently=False,
            )
        return HttpResponse('Check Your Mail For A Link. Click On It To Change Your Password')
    else:
        return render(req,'forgot.html')

def change_password(req):

    if req.method == 'GET':
        userId = req.GET['userId']
        token = req.GET['token']
        if PasswordToken.objects.filter(token=token).exists():
            return render(req,'changepass.html', {
                'userId': userId,
            })
    elif req.method == 'POST':
        userId = req.POST['userId']
        newPass = req.POST['newPass']
        user = User.objects.get(id=str(userId))
        user.set_password(newPass)
        user.save()
        return HttpResponse("Password Updated")
    else:
        return HttpResponse("Token expired or invalid")

        


