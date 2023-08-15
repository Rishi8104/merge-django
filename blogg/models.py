from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class Comment(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    #Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField()

    def __str__(self):
        return self.user.username +  " Comment: " + self.content

class User(AbstractUser):
    phone = models.IntegerField(default=0)
    
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, default=uuid.uuid4)
    
    def __str__(self):
        return str(self.user)


class Tag(models.Model):
    name = models.CharField(max_length=256 )
    slug = models.SlugField( unique= True, max_length=100,default=uuid.uuid4)
    Post = models.ManyToManyField('Post', related_name='tags')
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering=['-slug']
        
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"slug": self.slug})


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="Created at")
    updated_at  = models.DateTimeField ( auto_now_add=True, verbose_name="Updated at")
    title = models.CharField(max_length=300, verbose_name="Title",null=False,blank=False)
    slug = models.SlugField(unique=True, default=uuid.uuid4)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['created_at']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Post(models.Model):
    Image =models.ImageField(null=True,blank=True)
    author =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title =models.CharField(max_length=300 ,null=False,blank=False)
    text =models.TextField()
    category=models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL,related_name="Post_category")
    Tag = models.ManyToManyField(Tag ,related_name="Post_tags")
    Comment=models.ManyToManyField(Comment,related_name="Post_tags")
    create_date =  models.DateTimeField(default= timezone.now)
    published_date= models.DateTimeField(blank=True,null=True)
    slug =models.SlugField(unique=True, default=uuid.uuid4)

    def publish(self):
        self.publish_date= timezone.now()
        self.save()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
            return reverse("post_detail", kwargs={"slug": self.slug})

        
