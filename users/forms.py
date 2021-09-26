from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Profile, Skill, Message
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields  = ['first_name','email','username','password1','password2']
        labels = {'first_name':'Name',}

        #widgets = {
        #    'tags': forms.CheckboxSelectMultiple(),
        #}

    def __init__(self, *args, **kwargs):

        super(CustomUserCreationForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','username','location','email','short_intro',
            'bio','profile_image','social_github','social_twitter','social_linkedin',
            'social_youtube','social_website'        
        ]
        
    def __init__(self, *args, **kwargs):

        super(ProfileForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']
        
    def __init__(self, *args, **kwargs):

        super(SkillForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read','created','id','sender','recipient']

        #fileds = ['name','email','subject','body']
        #exclude = []
        
    def __init__(self, *args, **kwargs):

        super(MessageForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})