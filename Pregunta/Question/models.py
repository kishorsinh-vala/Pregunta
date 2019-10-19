from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Question TABLE
class Quiz(models.Model):
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    q_ques=models.CharField(verbose_name='Question', max_length=300,null=False)
    
    class Meta:
        verbose_name = ("Quiz")
        verbose_name_plural =("Quizs")

    def __str__(self):
        return self.q_ques

#Answer Table
class Answer(models.Model):
    q_id=models.ForeignKey("Quiz",verbose_name='Question Table ID',on_delete=models.CASCADE)
    a_ans=models.CharField(verbose_name='Answer', max_length=500)
    a_usr_nm=models.CharField( verbose_name="Username", max_length=50)

    class Meta:
        verbose_name = ("Answer")
        verbose_name_plural =("Answers")

    def __str__(self):
        return self.a_ans