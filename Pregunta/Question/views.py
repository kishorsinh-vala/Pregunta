from django.shortcuts import render,redirect
from .forms import GetQuestionForm,QuestionForm,AnswerForm,UserRegistrationForm,UserLogin
from .models import Quiz,Answer
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

#index (Login)
def indexView(request):
    form=UserLogin(request.POST or None)
    name=request.POST.get('username')
    pwd=request.POST.get('password')
    user=authenticate(username=name, password=pwd)
    request.session['user'] = name
    
    if user is not None:
        return redirect('/question/')
    else:
        context={
                'form':form
            }
    return render(request,'index.html',context)


#new Registration
def regView(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            request.session['user']=request.POST['username']
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'User Registered with {username} Username!')
            return redirect('/question/')
    else:    
        form=UserRegistrationForm()
    return render(request,'register.html',{'form':form})
    
# #Registration View
# def registerView(request):
#     user_frm=UserRegistrationForm(request.POST or None)
#     if user_frm.is_valid():
#         request.session['user']=request.POST['username']
#         user_frm.save()
#         return redirect('/question/')
#     context={
#             'frm':user_frm
#     }
#     return render(request,'register.html',context)

#question View
def questionView(request):
   get_que=Quiz.objects.all()
   context={
        'frm':get_que
    }
   return render(request,'question.html',context)

 #Answer View User Can Post Answer   
def answerView(request,id):
    userId=int(id)
    user_list=Quiz.objects.get(id=userId)
    a_ans=AnswerForm(request.POST or None)
    if request.method=='POST':
       uid1 = request.session['user']
       userobj = User.objects.get(username=uid1)
       answer=Answer()
       answer.q_id=user_list
       answer.a_usr_nm=userobj
       answer.a_ans=request.POST['a_ans']
       answer.save()
       return redirect('/question/')
    q_frm=QuestionForm(request.POST or None, instance=user_list)
    context={
        'ques':q_frm,
        'ans':a_ans,
    }
    return render(request,'answer.html',context)

    # uid1 = request.session['user']
    # userobj = User.objects.get(username=uid1)

#user ask Question
def usersQuestionView(request):
    frm=QuestionForm(request.POST or None)
    if  request.method=='POST':
        form=Quiz()
        uid1 = request.session['user']
        userobj = User.objects.get(username=uid1)
        ques=request.POST['q_ques']
        form.u_id=userobj
        form.q_ques=ques
        form.save()
        return redirect('/question/')
    context={
        'frm':frm
    }
    return render(request,'users_question.html',context)

def dispAnswer(request):
    uid1 = request.session['user']
    userobj = Answer.objects.get(username=uid1)
    context={
        'form':userobj
    }
    return render(request,'dispAnswer.html',context)