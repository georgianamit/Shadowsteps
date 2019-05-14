from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from account.models import Profile
from django.contrib.auth import authenticate, login, logout, get_user_model
from account.forms import SignInForm, SignUpForm, AvatarUploadForm, BioSettingForm, PersonalProfileSettingForm, PersonalUserSettingForm, HighSchoolSettingForm, GraduationSettingForm, PostGraduationSettingForm
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
            bio_form = BioSettingForm(instance=request.user.profile)
        
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
                profile.gender = personal_profile_form.cleaned_data['gender']
                profile.dob = personal_profile_form.cleaned_data['dob']
                profile.phone_no = personal_profile_form.cleaned_data['phone_no']
                profile.address = personal_profile_form.cleaned_data['address']
                profile.city = personal_profile_form.cleaned_data['city']
                profile.state = personal_profile_form.cleaned_data['state']
                profile.zip_code = personal_profile_form.cleaned_data['zip_code']
                profile.save()
                return redirect("account:setting")
        else:
            personal_profile_form = PersonalProfileSettingForm(instance=request.user.profile)
            personal_user_form = PersonalUserSettingForm(instance=request.user)

        if("update-high-school" in request.POST):
            hs_form = HighSchoolSettingForm(request.POST)
            if hs_form.is_valid():
                profile = Profile.objects.get(user=request.user)
                profile.high_school = hs_form.cleaned_data['high_school']
                profile.hs_year = hs_form.cleaned_data['hs_year']
                profile.hs_percentage = hs_form.cleaned_data['hs_percentage']
                profile.save()
                return redirect("account:setting")
        else:
            hs_form= HighSchoolSettingForm(instance=request.user.profile)
        
        if("update-graduation" in request.POST):
            g_form = GraduationSettingForm(request.POST)
            if g_form.is_valid():
                profile = Profile.objects.get(user=request.user)
                profile.g_college = g_form.cleaned_data['g_college']
                profile.g_degree = g_form.cleaned_data['g_degree']
                profile.g_branch = g_form.cleaned_data['g_branch']
                profile.g_year = g_form.cleaned_data['g_year']
                profile.g_cgpa = g_form.cleaned_data['g_cgpa']
                profile.save()
                return redirect("account:setting")
        else:
            g_form= GraduationSettingForm(instance=request.user.profile)
        
        if("update-post-graduation" in request.POST):
            pg_form = PostGraduationSettingForm(request.POST)
            if pg_form.is_valid():
                profile = Profile.objects.get(user=request.user)
                profile.pg_college = pg_form.cleaned_data['pg_college']
                profile.pg_degree = pg_form.cleaned_data['pg_degree']
                profile.pg_branch = pg_form.cleaned_data['pg_branch']
                profile.pg_year = pg_form.cleaned_data['pg_year']
                profile.pg_cgpa = pg_form.cleaned_data['pg_cgpa']
                profile.save()
                return redirect("account:setting")
        else:
            pg_form= PostGraduationSettingForm(instance=request.user.profile)           


    else:
        image_form = AvatarUploadForm()
        bio_form = BioSettingForm(instance=request.user.profile)
        personal_profile_form = PersonalProfileSettingForm(instance=request.user.profile)
        personal_user_form = PersonalUserSettingForm(instance=request.user)
        hs_form= HighSchoolSettingForm(instance=request.user.profile)
        g_form= GraduationSettingForm(instance=request.user.profile)
        pg_form= PostGraduationSettingForm(instance=request.user.profile)           


    context = {
        'navbar': False,
        'image_form':image_form,
        'bio_form':bio_form,
        'personal_profile_form':personal_profile_form,
        'personal_user_form':personal_user_form,
        'hs_form':hs_form,
        'g_form':g_form,
        'pg_form':pg_form,
    }

    return render(request, "account/settings.html", context)
