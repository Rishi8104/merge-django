from django import forms
from .models import Post,User,Comment
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','Image', 'text','category','Tag')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UsProfile
#         fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )

class NewUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' ,'first_name','last_name' ,'email' ,'password1','password2','phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image',]

def save(self,commit=True):
     user = super(NewUserFrom,self).save(commit=False)
     user.email = self.cleaned_data['email']
     if commit :
            user.save()
            return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')