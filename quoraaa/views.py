from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
import datetime
from quoraaa.models import PostQuestion,Answer
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# Create your views here.
def render_login(request):
    return render(request,"login.html")
# if user is existed redirect the user_profile_return_home 



def perform_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')
        user_obj = authenticate(request,username=username,password=password)
        print(user_obj)
        if user_obj is not None:
            login(request,user_obj)
            questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
            return render(request,'dashboard_page.html',{'questions':questions_list})
        else:
            return HttpResponseRedirect('/')
    else :
        questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
        return render(request,'dashboard_page.html',{'questions':questions_list})

def register_page(request):
    return render(request,'registration_page.html')

def perform_registration(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
       
        user_obj=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
        user_obj.save()
        return render(request,"login.html")
    else:
        return HttpResponse('Registration failed.')


def post_question(request):
    if request.method == 'POST':
        question=request.POST.get('question')
        posted_by=request.user
        form = PostQuestion(question=question,posted_by_id=posted_by.id,created_at=datetime.datetime.now())
        
        form.save()
        # post_question=PostQuestion.objects.create_user(question=question,posted_by=posted_by)
        # post_question.save()
        questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
            
        return render(request,'dashboard_page.html',{'questions':questions_list})
        # return render(request,"dashboard_page.html")
    else:
        return HttpResponse('')
    
def post_answer(request,id):
    if request.method == 'POST':
        # print(pk)
        answer=request.POST.get('answer')
        question=id
        question_id=PostQuestion.objects.get(id=id)
        
        user_details=User.objects.get(id=question_id.posted_by_id)
        form = Answer(answer=answer,question_id=question,created_at=datetime.datetime.now(),answer_by=user_details)
        
        form.save()
        # post_question=PostQuestion.objects.create_user(question=question,posted_by=posted_by)
        # post_question.save()
        questions_list= PostQuestion.objects.all().order_by('created_at').reverse()
            
        return render(request,'dashboard_page.html',{'questions':questions_list})
        # return render(request,"dashboard_page.html")
    else:
       
        return HttpResponse('Error')
    
def view_answer(request,id):
    if request.method == 'GET':
        answer_list= Answer.objects.filter(question_id=id).all()
        
        # print(user_details)
        # return HttpResponse(request,{'answers':answer_list})
        return render(request,"answers.html",{'answers':answer_list})
    else:
        return HttpResponse('Error')

def like_answer(request,id,st):
    if request.method == 'GET':
        print(st)
        if st=='true':
         Answer.objects.filter(id=id).update(liked=True)
        else:
           Answer.objects.filter(id=id).update(liked=False) 
        ans_details=Answer.objects.get(id=id)
        answer_list= Answer.objects.filter(question_id=ans_details.question_id).all()
        return render(request,"answers.html",{'answers':answer_list})
    

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    
    return redirect('/')