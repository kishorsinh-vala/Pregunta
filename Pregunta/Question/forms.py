from django import forms
from Question.models import User,Quiz,Answer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

Radio_Choice=[
        ('male','Male'),
        ('female','Female')
    ]
#Stream
Choice_streem=[
    ('bca_fy','BCA FY'),
    ('bca_sy','BCA SY'),
    ('bca_ty','BCA TY'),
    ('bscIt_fy','BScIT FY'),
    ('bscIt_sy','BScIT SY'),
    ('bscIt_ty','BScIT TY'),
    ('mscIt_fy','MScIT FY'),
    ('mscIt_sy','MScIT SY')
]
# class ShoppingForm(forms.Form):
#     u_nm=forms.CharField(label='User Name')
#     u_pwd=forms.CharField(label='Password')
#     u_email=forms.EmailField(label='Email')
#     u_contact=forms.CharField(label='Contact')
#     u_gender=forms.CharField(label='Gender')

# class UserForm(forms.ModelForm):
#     u_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
#     u_pass=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
#     u_email=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
#     u_gender=forms.CharField(label='Gender',widget=forms.RadioSelect(choices=Radio_Choice))
#     #u_streem=forms.CharField(label='Gender',widget=forms.ChoiceField( choices=Choice_streem))
#     u_streem = forms.ChoiceField(label='sdsd', choices=Choice_streem, required=False)
#     u_cno=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Mobile No'}),max_length=10)
#     class Meta:
#         model=User
#         fields = '__all__'

class QuestionForm(forms.ModelForm):
    u_id=forms.CharField(label='User Id',widget=forms.TextInput(attrs={'class':'form-control'}))
    q_ques=forms.CharField(label='Question',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Quiz
        fields='__all__'    

class GetQuestionForm(forms.ModelForm):
    u_id=forms.CharField(label='User Id',widget=forms.TextInput(attrs={'class':'form-control'}))
    q_ques=forms.CharField(label='Question',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Quiz
        fields='__all__'

class AnswerForm(forms.ModelForm):
    a_ans=forms.CharField(label='Answer',widget=forms.Textarea)
    class Meta:
        model=Answer
        fields='__all__'

        #userRegistrationForm
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email','class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username','class':'form-control'}))
    password1=forms.CharField(label='Password',min_length=8,widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'form-control'}))
    password2=forms.CharField(label='Password',min_length=8,widget=forms.PasswordInput(attrs={'placeholder':'Re-Type Password','class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
    # def clean_password2(self):
    #     p1=self.cleaned_data['password1']
    #     p2=self.cleaned_data['password2']
    #     if p1!= p2:
    #         raise ValidationError('Password Doesnot Matched')
    #     return p1
    def clean_password2(self):
        data = self.cleaned_data["password2"]
        data1= self.cleaned_data["password1"]
        self.fields['password1'].widget.attrs.pop("autofocus", None)
        if data1 != data:
            raise ValidationError("Password Doesn't Match")
        return data1

class UserLogin(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username','class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'form-control'}))
   
    class Meta:
        model=User
        fields='__all__'
    
    