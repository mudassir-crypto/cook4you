from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import Education, Experience, Profile, Cuisine, Message
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']

        labels = {
            "first_name": "Full Name",
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email is already registered!")

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['resume'].widget.attrs['placeholder'] = 'Drive link to your Resume'
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})