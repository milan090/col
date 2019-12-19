from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='forum'),
    path('ask', views.ask, name='ask'),
    path('Question', views.question, name='question')
]