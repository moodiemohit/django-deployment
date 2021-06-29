from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout,authenticate,login

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def register(request):
    form = UserForm()
    form1 = UserProfileInfoForm()
    dic = {'form':form,'form1':form1}

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile= profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

        profile.save()

    return render(request,'userloginapp/register.html',dic)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('USer NOt active')
        else:
            print('someone tried to log into & failed')
            return HttpResponse('Invalid Login credentials')


    return render(request,'userloginapp/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
