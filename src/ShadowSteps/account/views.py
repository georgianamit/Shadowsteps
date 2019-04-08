from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from account.models import Profile
from django.contrib.auth import authenticate, login, logout, get_user_model
from account.forms import SignInForm, SignUpForm, AvatarUploadForm
from django.http import HttpResponseRedirect

# Create your views here.
User = get_user_model()

def profileView(request, slug):
    user = User.objects.filter(username__iexact=slug).first()
    
    context={
        'user': user,
        'navbar': True,
    }
    if not request.user.is_authenticated:
        return redirect("account:signin")       
    else:
        return render(request,"account/profile.html", context)

def signInView(request):
    form = SignInForm(None or request.POST)
    if form.is_valid():
        username_ = form.cleaned_data.get('username')
        user_obj = User.objects.filter(username__iexact=username_).first()
        login(request, user_obj)
        print(user_obj)
        return redirect("account:profile", slug = username_)
    
    context = {
        'form': form,
        'navbar': True,
    }


    return render(request, "account/signin.html", context)

def signUpView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:profile", slug = username)
    else:
        form = SignUpForm()
    
    context = {
        'form': form,
        'navbar': True,
    }


    return render(request, "account/signup.html", context)

def signOutView(request):
    logout(request)
    return redirect("account:signin")

def settingView(request):
    if(request.method == "POST"):
        image_form = AvatarUploadForm(request.POST, request.FILES)
        if image_form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.image=image_form.cleaned_data['avatar']
            profile.save()
            return redirect("account:setting")
    else:
        image_form = AvatarUploadForm()

    context = {
        'navbar': False,
        'image_form':image_form,
    }

    return render(request, "account/settings.html", context)
