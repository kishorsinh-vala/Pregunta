from django.conf.urls import url
from django.contrib import admin
from Question import views

urlpatterns = [
    url('index/', views.indexView, name='index'),
    # url('register/',views.registerView,name='register'),
    url('question/',views.questionView,name='question'),
    url('answer/(?P<id>\d+)/$',views.answerView,name='answer'),
    url('usersQuestion/',views.usersQuestionView,name='userQuestion'),
    url('usersAnswer/',views.dispAnswer,name='users_answer')
]