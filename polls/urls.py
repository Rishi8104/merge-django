from django.urls import path
from . import views
app_name="polls"
urlpatterns =[
    path("",views.indexView.as_view(), name='index'), 
    path("<slug:slug>/", views.DetailView.as_view(), name="detail"),
    path("<slug:slug>/results/", views.ResultsView.as_view(), name="results"),
    path("<slug:question_slug>/vote/", views.vote, name="vote"),
]