from django import forms
from django.contrib.auth.models import User
from .models import Profile, UserLanguage, UserFramework, UserPlatform
import datetime
from account.choices import GENDER_CHOICES, LEVEL_CHOICES, LANGUAGE_CHOICES, FRAMEWORK_CHOICES, PLATFORM_CHOICES


class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Username"
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-email",
            'placeholder': "Email"
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'id': "form1-password1",
            'placeholder': "Password"
        }
    ))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'id': "form1-password2",
            'placeholder': "Confirm Password"
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
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Username"
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'id': "form1-password",
            'placeholder': "Password"
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            raise forms.ValidationError('Invalid credentials')
        else:
            if not user_obj.check_password(password):
                raise forms.ValidationError('Invalid Credentials')
        return super(SignInForm, self).clean(*args, **kwargs)


class AvatarUploadForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=True,
    )

    class Meta:
        model = Profile
        fields = (
            'avatar',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'filestyle'
        self.fields['avatar'].widget.attrs['style'] = 'display:none'
        self.fields['avatar'].widget.attrs['id'] = 'browsefield'


class BioSettingForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Bio",
            'rows': 3,
        }
    ))
    motto = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-email",
            'placeholder': "Motto",
            'rows': 2
        }
    ))

    class Meta:
        model = Profile
        fields = (
            'bio',
            'motto',
        )


class PersonalProfileSettingForm(forms.ModelForm):

    dob = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, datetime.date.today().year+1),
        attrs={
            'class': "form-control dob-horizontal",
        }
    ))
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': "form-control",
                'id': "form1-gender",
            }
        ))
    phone_no = forms.CharField(error_messages={'max_length': 'More than 10 digits.'}, widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Phone No.",
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Address",
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "City",
        }
    ))
    state = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "State",
        }
    ))
    zip_code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Zip Code",
        }
    ))

    class Meta:
        model = Profile
        fields = ("gender", "dob", "phone_no",
                  "address", "state", "city", "zip_code")


class PersonalUserSettingForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "First Name",
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Last Name",
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-username",
            'placeholder': "Email",
        }
    ))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class HighSchoolSettingForm(forms.ModelForm):
    high_school = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-high-school",
            'placeholder': "High School Name",
        }
    ))
    hs_year = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-year",
            'placeholder': "Year",
        }
    ))
    hs_percentage = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-percentage",
            'placeholder': "Percentage",
        }
    ))

    class Meta:
        model = Profile
        fields = ("high_school", "hs_year", "hs_percentage")


class GraduationSettingForm(forms.ModelForm):
    g_college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-high-school",
            'placeholder': "College/Institude Name",
        }
    ))
    g_degree = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-year",
            'placeholder': "Degree",
        }
    ))
    g_branch = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-percentage",
            'placeholder': "Branch",
        }
    ))
    g_year = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-percentage",
            'placeholder': "Graduation Year",
        }
    ))
    g_cgpa = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-percentage",
            'placeholder': "CGPA",
        }
    ))

    class Meta:
        model = Profile
        fields = ("g_college", "g_degree", "g_branch", "g_year", "g_cgpa")


class PostGraduationSettingForm(forms.ModelForm):
    pg_college = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-high-school",
            'placeholder': "College/Institude Name",
        }
    ))
    pg_degree = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-year",
            'placeholder': "Degree",
        }
    ))
    pg_branch = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-percentage",
            'placeholder': "Branch",
        }
    ))
    pg_year = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-percentage",
            'placeholder': "Graduation Year",
        }
    ))
    pg_cgpa = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'id': "form1-hs-percentage",
            'placeholder': "CGPA",
        }
    ))

    class Meta:
        model = Profile
        fields = ("pg_college", "pg_degree", "pg_branch", "pg_year", "pg_cgpa")


class LanguageSettingForm(forms.ModelForm):
    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': "form-control",
                'id': "language",
            }
        ))
    level = forms.ChoiceField(
        choices=LEVEL_CHOICES,
        widget=forms.Select(
            attrs={
                'class': "form-control",
                'id': "lang-level",
            }
        ))

    class Meta:
        model = UserLanguage
        fields = ('language', 'level')

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     user = self.request.user
    #     l = cleaned_data.get('language')
    #     u = UserLanguage.objects.filter(user=user, language=l)

    #     level = cleaned_data.get('level')
    #     print(cleaned_data, user, l, u, level)
    #     if u.level == level:
    #         raise ValidationError("This Language is already in your skill.")
    #     else:
    #         return self.cleaned_data


class FrameworkSettingForm(forms.ModelForm):
    framework = forms.ChoiceField(
        choices=FRAMEWORK_CHOICES,
        widget=forms.Select(
            attrs={
                'class': "form-control",
                'id': "framework",
            }
        ))
    level = forms.ChoiceField(
        choices=LEVEL_CHOICES,
        widget=forms.Select(
            attrs={
                'class': "form-control",
                'id': "fw-level",
            }
        ))

    class Meta:
        model = UserFramework
        fields = ('framework', 'level')


class PlatformSettingForm(forms.ModelForm):
    platform = forms.ChoiceField(
        choices=PLATFORM_CHOICES,
        widget=forms.Select(
            attrs={
                'class': "form-control",
                'id': "platform",
            }
        ))
    level = forms.ChoiceField(
        choices=LEVEL_CHOICES,
        widget=forms.Select(
            attrs={
                'class': "form-control",
                'id': "pf-level",
            }
        ))

    class Meta:
        model = UserPlatform
        fields = ('platform', 'level')
