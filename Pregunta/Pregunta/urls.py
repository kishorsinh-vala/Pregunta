
from django.contrib import admin
from django.urls import path,include
from Question import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_view.regView,name='register'),
    path('',include('Question.urls')),
    path('',user_view.indexView,name='index')
]
