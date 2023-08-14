from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice

class indexView(generic.ListView):
    template_name= "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
    

#return HttpResponse("Hello, World. You'ar at the polls index.")
    

class DetailView(generic.DetailView):
    ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request,question_slug):
    question = get_object_or_404(Question,slug=question_slug)
    try:
        selected_choice = question.choice_set.get(slug=request.POST["choice"])
    except(KeyError,Choice.DoesNotExists):
        return render(
            request,"polls/detail.html",
            {
                'question':question,
                'error':'you didnt select a choice.'
            },
        )                                             
        
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.slug,)))

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context={ 
        "latest_question_list":latest_question_list,
        "qlist":True
             }
    return HttpResponse(template.render(context, request))

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
def results(request, question_slug):
    question = get_object_or_404(Question, slug = question_slug)
    return render(request, "polls/results.html", {"question": question})

def detail(request, question_slug):
    question = get_object_or_404(Question, slug = question_slug)
    return render(request, "polls/detail.html", {"question": question})
    

    
    