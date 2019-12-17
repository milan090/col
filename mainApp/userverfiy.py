import uuid
from .models import UserToken
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail

def fn_generate_token(userId, domain):
    if userId > 0:
        exists = UserToken.objects.filter(userId=userId).exists()
        if not exists:
            token = uuid.uuid4()
            link = 'http://{}/ActivateUser?token={}&userId={}'.format(domain,token, userId)
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
            send_mail(
                'Account confirmed - COL',
                'Now you can login to your account \n https://127.0.0.1:8000/login '
                'milanmuhammed1@gmail.com',
                [user_obj.email],
                fail_silently=False,
            )
            return HttpResponse('user activated')
        return HttpResponse('invalid token')
    except Exception as identifier:
        pass