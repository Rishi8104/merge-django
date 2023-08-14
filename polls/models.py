import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.urls import reverse
import uuid

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('Question', max_length=200 , null=False,blank=False)
    pub_date = models.DateTimeField("date published" , null=False,blank=False)
    slug = models.SlugField(  unique=True,default=uuid.uuid4)
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="published recently?",
    )

    

    def was_published_recently(self):
        now = timezone.now()
        return now -datetime.timedelta(days=1)<= self.pub_date <= now 

        
    def __str__(self):
        return self.question_text
    
    def get_absolute_url(self):
            return reverse("question_detail", kwargs={"slug": self.slug})
        
    
    

class Choice(models.Model):
    Question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True,default=uuid.uuid4)

    def __str__(self):
        return self.choice_text
    def get_absolute_url(self):
            return reverse("results", kwargs={"slug": self.slug})
  