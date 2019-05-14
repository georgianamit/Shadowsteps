from django import forms
from django.contrib.auth.models import User
from .models import Profile
import datetime

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Username"
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-email",
            'placeholder':"Email"
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':"form-control",
            'id':"form1-password1",
            'placeholder':"Password"
        }
    ))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={
            'class':"form-control",
            'id':"form1-password2",
            'placeholder':"Confirm Password"
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Username"
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':"form-control",
            'id':"form1-password",
            'placeholder':"Password"
        }
    ))


    class Meta:
        model = User
        fields = ('username','password')
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user_obj = User.objects.filter(username = username).first()
        if not user_obj:
            raise forms.ValidationError('Invalid credentials')
        else:
            if not user_obj.check_password(password):
                raise forms.ValidationError('Invalid Credentials')
        return super(SignInForm, self).clean(*args, **kwargs)

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=(
            'avatar',
        )

class BioSettingForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Bio",
            'rows':3,
        }
    ))
    motto = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-email",
            'placeholder':"Motto",
            'rows':2
        }
    ))
    class Meta:
        model = Profile
        fields=(
            'bio',
            'motto',
        )

class PersonalProfileSettingForm(forms.ModelForm):
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    dob = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, datetime.date.today().year+1),
        attrs={
            'class':"form-control",
        }
    ))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(
        attrs={
            'class':"form-control",
            'id':"form1-gender",
        }
    ))
    phone_no = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Phone No.",
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Address",
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"City",
        }
    ))
    state = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"State",
        }
    ))
    zip_code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Zip Code",
        }
    ))
    class Meta:
        model = Profile
        fields = ("gender", "dob", "phone_no", "address", "state", "city", "zip_code")

class PersonalUserSettingForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"First Name",
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Last Name",
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Email",
        }
    ))
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class HighSchoolSettingForm(forms.ModelForm):
    high_school = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-high-school",
            'placeholder':"High School Name",
        }
    ))
    hs_year = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-year",
            'placeholder':"Year",
        }
    ))
    hs_percentage = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-percentage",
            'placeholder':"Percentage",
        }
    ))

    class Meta:
        model=Profile
        fields=("high_school", "hs_year","hs_percentage")

class GraduationSettingForm(forms.ModelForm):
    g_college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-high-school",
            'placeholder':"College/Institude Name",
        }
    ))
    g_degree = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-year",
            'placeholder':"Degree",
        }
    ))
    g_branch = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-percentage",
            'placeholder':"Branch",
        }
    ))
    g_year = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-percentage",
            'placeholder':"Graduation Year",
        }
    ))
    g_cgpa = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-percentage",
            'placeholder':"CGPA",
        }
    )) 

    class Meta:
        model=Profile
        fields=("g_college", "g_degree", "g_branch", "g_year", "g_cgpa")

class PostGraduationSettingForm(forms.ModelForm):
    pg_college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-high-school",
            'placeholder':"College/Institude Name",
        }
    ))
    pg_degree = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-year",
            'placeholder':"Degree",
        }
    ))
    pg_branch = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-percentage",
            'placeholder':"Branch",
        }
    ))
    pg_year = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-percentage",
            'placeholder':"Graduation Year",
        }
    ))
    pg_cgpa = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-hs-percentage",
            'placeholder':"CGPA",
        }
    ))
    class Meta:
        model=Profile
        fields=("pg_college", "pg_degree", "pg_branch", "pg_year", "pg_cgpa")
