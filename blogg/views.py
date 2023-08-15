from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from django.utils import timezone
from .models import Post,Category,Tag,User
from .forms import PostForm,ProfileForm,NewUserFrom
# from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


# Create your views here.

def post_list(request):
    posts=Post.objects.all().order_by('-slug')
    return render(request, 'blog/post_list.html',{'posts':posts})
    

def post_detail(request,slug):
    Post.objects.get(slug=slug)
    post = get_object_or_404(Post,slug=slug)
    return render(request, 'blog/post_detail.html',{'post':post})

# def blogs_comments(request, slug):
#     post= Post.objects.filter(slug=slug).first()
#     comments= Comment.objects.filter(blog=post)
#     if request.method == "POST":
#         user= request.user
#         content= request.POST.get('content','')
#         blog_id=request.POST.get('blog_id','')
#         comment=Comment(user=user,content=content,blog=post)
#         comment.save()
#     return render(request,"blog_comments.html",{'post':post,'comments':comments})

# def reply_Blog_Post(request,slug)
#     posts=Post.objects.get(slug=slug)
#     if request.method=="POST":
#         posts.delete()
#         return redirect('/')
#     return render(request, 'reply_blog_post.html',{'posts':posts})
@login_required(login_url = 'blog/login_detail.html')
def post_new(request):
    form = PostForm(request.post,)
    return render(request, 'blog/post_edit.html',{'from':form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def category_list(request):
    categories=Category.objects.all().order_by('-slug')
    return render ( request,'blog/category_list.html',{'categories':categories})

def category_detail(request, slug):
    # Category.objects.get(slug=slug)
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/category_detail.html', {'category': category})

def Tags_list(request):
    Tags=Tag.objects.all().order_by('name')
    return render ( request,'blog/Tag_list.html',{'Tags':Tags})

def Tag_detail(request, slug):
    # Tag.objects.get(slug=slug)
    TagOjb = get_object_or_404(Tag, slug=slug)
    return render(request, 'blog/Tag_detail.html', {'Tag': TagOjb})

def sign_up(request):
    if request.method=='POST':
        form= NewUserFrom(request.POST)
        #print(form)
        if form.is_valid():
            User=form.save()
            login(request,User)
            messages.success(request,"Registration successful.")
            return redirect('login_detail')
        return render (request=request, template_name="blog/sign_up.html", context={})
    return render(request,'blog/sign_up.html')

def login_detail(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            print("Successfully Logged IN!!")
            return redirect('Post_list')
        else:
            messages.error( request,"Username or password is incorrect !!!")
        return render(request,'blog/Post_list.html')
    return render(request, "blog/login_detail.html")


def LogoutPage(request):
    logout(request)
    messages.success(request,"Successfully Logged Out !")
    return redirect('blog/login_detail')

def User_Profile(request,slug):
    
    post = Post.objects.filter(Post,slug=slug)
    post = get_object_or_404(Post, slug=slug)
    return render(request,"blog/user_profile.html",{'Post':post})

def Profile(request):
    return render(request, "blog/profile.html")

def update_profile(request):
    try:
        uprofile = request.user.Profile
    except: Profile.DoesNotExist
    uprofile = Profile(user=request.user)
    if request.method=="POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=uprofile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "blog/update_profile.html", {'alert':alert})
    else:
        form=ProfileForm(instance=uprofile)
    return render(request, "blog/update_profile.html", {'form':form})
    
    
