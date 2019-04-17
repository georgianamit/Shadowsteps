from django import forms
from django.contrib.auth.models import User
from .models import Profile

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
    bio = forms.CharField(widget=forms.TextInput(
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
        fields = ("phone_no", "address", "state", "city", "zip_code")

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
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':"form-control",
            'id':"form1-username",
            'placeholder':"Email",
        }
    ))
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
