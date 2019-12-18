from django.urls import path
from . import views
from .userverfiy import fn_verify_token, forgot_password, change_password

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('ActivateUser', fn_verify_token),
    path('profile', views.profile, name='user_profile'),
    path('ForgotPassword', forgot_password),
    path('ChangePassword', change_password),
]