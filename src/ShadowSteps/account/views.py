from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from account.models import Profile
from django.contrib.auth import authenticate, login, logout, get_user_model
from account.forms import SignInForm, SignUpForm, AvatarUploadForm, BioSettingForm, PersonalProfileSettingForm, PersonalUserSettingForm
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
        if 'upload-avatar' in request.POST:
            image_form = AvatarUploadForm(request.POST, request.FILES)
            if image_form.is_valid():
                profile = Profile.objects.get(user=request.user)
                profile.avatar=image_form.cleaned_data['avatar']
                profile.save()
                return redirect("account:setting")
        else:
            image_form = AvatarUploadForm()
            
        if 'update-bio' in request.POST:
            bio_form = BioSettingForm(request.POST)
            if bio_form.is_valid():
                profile = Profile.objects.get(user= request.user)
                profile.bio = bio_form.cleaned_data['bio']
                profile.motto = bio_form.cleaned_data['motto']
                profile.save()
                return redirect("account:setting")
        else:
            bio_form = BioSettingForm()
        
        if 'update-personal' in request.POST:
            personal_profile_form = PersonalProfileSettingForm(request.POST)
            personal_user_form = PersonalUserSettingForm(request.POST)
            if personal_profile_form.is_valid() and personal_user_form.is_valid():
                print("submitting")
                profile = Profile.objects.get(user=request.user)
                user = User.objects.get(username = request.user)
                user.first_name = personal_user_form.cleaned_data['first_name']
                user.last_name = personal_user_form.cleaned_data['last_name']
                user.email = personal_user_form.cleaned_data['email']
                user.save()
                profile.phone_no = personal_profile_form.cleaned_data['phone_no']
                profile.address = personal_profile_form.cleaned_data['address']
                profile.city = personal_profile_form.cleaned_data['city']
                profile.state = personal_profile_form.cleaned_data['state']
                profile.zip_code = personal_profile_form.cleaned_data['zip_code']
                profile.save()
                return redirect("account:setting")
        else:
            personal_profile_form = PersonalProfileSettingForm()
            personal_user_form = PersonalUserSettingForm()

    else:
        image_form = AvatarUploadForm()
        bio_form = BioSettingForm()
        personal_profile_form = PersonalProfileSettingForm()
        personal_user_form = PersonalUserSettingForm()

    context = {
        'navbar': False,
        'image_form':image_form,
        'bio_form':bio_form,
        'personal_profile_form':personal_profile_form,
        'personal_user_form':personal_user_form,
        'day_range': range(1,32),
        'month_range': range(1,13),
        'year_range': range(2010,1950,-1),
    }

    return render(request, "account/settings.html", context)
