import uuid
from .models import UserToken
from django.contrib.auth.models import User
from django.http import HttpResponse

def fn_generate_token(userId):
    if userId > 0:
        exists = UserToken.objects.filter(userId=userId).exists()
        if not exists:
            token = uuid.uuid4()
            link = 'http://127.0.0.1:8000/ActivateUser?token={}&userId={}'.format(token, userId)
            user_token_obj = UserToken(token=token, userId=userId, link=link)
            user_token_obj.save()


def fn_verify_token(req):
    try:
        user_id = req.GET['userId']
        verify = UserToken.objects.filter(userId=user_id, token=req.GET['token']).exists()
        if verify:
            user_obj = User.objects.get(id=user_id)
            user_obj.is_active = True
            user_obj.save()
            UserToken.objects.get(userId=user_id).delete()
            return HttpResponse('user activated')
        return HttpResponse('invalid token')
    except Exception as identifier:
        pass