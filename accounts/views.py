from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .forms import  ProfileRegisterForm , ProfileEditForm ,UserEditForm
from .models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request , username=username ,password=password)
        if user :
            login(request,user)
            return redirect('account:profile')
    return render(request,'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('/')



def profileregister(request):
    if request.method == "POST":
        profileRegisterForm = ProfileRegisterForm(request.POST, request.FILES)
        if profileRegisterForm.is_valid():
            username = profileRegisterForm.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                context = {
                    "formData": profileRegisterForm,
                    "errorMessage": "Username already exists. Please choose a different username."
                }
                return render(request, "accounts/sign-up.html", context)

            user = User.objects.create_user(
                username=username,
                email=profileRegisterForm.cleaned_data['email'],
                password=profileRegisterForm.cleaned_data['password'],
                first_name=profileRegisterForm.cleaned_data['first_name'],
                last_name=profileRegisterForm.cleaned_data['last_name']
            )
            user.save()

            profilemodel = UserProfile(
                user=user,
                profile_picture=profileRegisterForm.cleaned_data['profile_picture'],
                Gender=profileRegisterForm.cleaned_data['Gender'],
                phone=profileRegisterForm.cleaned_data['phone'],
                address=profileRegisterForm.cleaned_data['address']
            )
            profilemodel.save()

            #send email
            # subject = 'Welcome to Our Site!'
            # html_message = render_to_string('emails/welcome_email.html', {'user': user})
            # plain_message = strip_tags(html_message)
            # from_email = 'your_email@gmail.com'
            # to = user.email

            # send_mail(subject, plain_message, from_email, [to], html_message=html_message)



            return HttpResponseRedirect(reverse("home:home"))
        else:
            print(profileRegisterForm.errors)
    else:
        profileRegisterForm = ProfileRegisterForm()

    context = {
        "formData": profileRegisterForm
    }

    return render(request, "accounts/sign-up.html", context)




@login_required
def profile_view(request):
    profile=request.user.profile
    photo=request.user.profile.profile_picture

    context = {
        "profile" : profile,
        "photo" : photo,
    }
    return render(request,'accounts/profile.html',context)



def ProfileEdit(request):
    if request.method=="POST":
        profileEditForm = ProfileEditForm(request.POST,request.FILES,instance=request.user.profile)
        userEditForm=UserEditForm(request.POST,instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse("account:profile"))
    else:
        profileEditForm=ProfileEditForm(instance=request.user.profile)
        userEditForm=UserEditForm(instance=request.user)


    context={
        "profileEditForm":profileEditForm,
        'userEditForm':userEditForm,
        'profileImage':request.user.profile.profile_picture,
    }

    return render(request,"accounts/Edit.html",context)