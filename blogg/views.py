from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect
from django.utils import timezone
from .models import Post,Category,Tag,Comment
from .forms import PostForm,NewUserFrom,NewUserFrom,CommentForm
# from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


# Create your views here.

def post_list(request):
    posts=Post.objects.all().order_by('-slug')
    return render(request, 'blog/post_list.html',{'posts':posts})
    

def post_detail(request,slug):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post,slug=slug)
    comments = Comment.objects.filter(active=True, parent__isnull= True)     #post=self.get_object()
    print("comments")
    new_comment=None #comment posted
    if request.method== 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj=None
            try:
                parent_id=int(request.POST.get('parent_id'))
            except: parent_id=None
                
            if parent_id:
                parent_obj = Comment.objects.get(id= parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm() 
    return render(request,template_name,{'post':post,
                                          'Comment': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

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
        form = PostForm(request.POST, instance=post, files=request.FILES)
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
        usrnm = User.object.get(username=username)
        print(usrnm)
        email=request.POST.get('username')
        print (email)
        print('username',username)
        pass1=request.POST.get('pass1')
        print('password',pass1)
        User=authenticate(request,username=username,password=pass1)
        if User is not None:
            login(request,User)
            print("Successfully Logged IN!!")
            return redirect('post_list')
        else:
            messages.error( request,"Username or password is incorrect !!!")
        return render(request,'blog/user_profile.html')
    return render(request, "blog/login_detail.html")


def LogoutPage(request):
    logout(request)
    messages.success(request,"Successfully Logged Out !")
    return redirect('login_detail')

def User_Profile(request,slug):
    post = Post.objects.filter(Post,slug=slug)
    post = get_object_or_404(Post, slug=slug)
    return render(request,"blog/user_profile.html",{'Post':post})

def Profile(request):
    user = request.user
    print('User Name :',user.username)
    return render(request, "blog/user_profile.html", {'user':user})

def update_profile(request):
    # try:
    #     profile = request.user.profile
    # except Profile.DoesNotExist:
    #     pass
    #     profile = Profile(user=request.user)
    
    if request.method == "POST":
        form = NewUserFrom(data=request.POST, instance=request.user, files=request.FILES, )
        
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "blog/update_profile.html", {'alert': alert})
    else:
        form = NewUserFrom(instance=request.user)
        
    
    return render(request, "blog/update_profile.html", {'form': form})

 