from django.urls import path
from . import views
appname='blogg'
urlpatterns = [
    path('',views.post_list,name ='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/slug', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('category',views.category_list, name='category_list'),
    path('categories/<slug>', views.category_detail, name= 'category_detail'),
    path('Tag',views.Tags_list,name="Tag_list"),
    path('Tag/<slug>', views.Tag_detail, name= 'Tag_detail'),
    path('signup/', views.sign_up, name='sign_up'),
    path("login/", views.login_detail, name="login_detail"),
    path( "logout/", views.LogoutPage , name="logout"),
    ]