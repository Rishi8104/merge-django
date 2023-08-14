from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from django.utils import timezone
from .models import Post,Category,Tag
from .forms import PostForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate 


# Create your views here.

def post_list(request):
    posts=Post.objects.all().order_by('-slug')
    return render(request, 'blog/post_list.html',{'posts':posts})
    

def post_detail(request,slug):
    Post.objects.get(slug=slug)
    post = get_object_or_404(Post,slug=slug)
    return render(request, 'blog/post_detail.html',{'post':post})
    
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
        fname=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not same !!")
        else:
            usr_obj = User.objects.create(first_name=fname,last_name=last_name,username=username,email=email,pass1=pass1,)
            # print(first_name)
            usr_obj.save()
            return redirect('blog/login_detail.html')
            

    return render(request,'blog/sign_up.html')

def login_detail(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            print("user password is correct1!!")
            return redirect('blog/post_list.html')
        else:
            return HttpResponse("Username or password is incorrect !!!")
    return render(request,'blog/login_detail.html')

def LogoutPage(request):
    logout(request)
    return redirect('blog/login_detail.html')
    
