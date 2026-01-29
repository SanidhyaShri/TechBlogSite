# from django.shortcuts import render

# # Create your views here.

# from .models import Post



# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'posts/home.html', {'posts': posts}) 


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect

# @login_required
# def add_post(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         content = request.POST['content']
#         Post.objects.create(title=title, content=content)
#         return redirect('/')
    
#     return render(request, 'posts/add_post.html')


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Post


# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'posts/home.html', {'posts': posts})


# @login_required
# def add_post(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         content = request.POST['content']
#         Post.objects.create(
#             title=title,
#             content=content,
#             author=request.user
#         )

#         return redirect('/')
    
#     return render(request, 'posts/add_post.html')


# # 👇 ADD THIS BELOW add_post (Delete Button - NEW FUNCTION)

# @login_required
# def delete_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.delete()
#     return redirect('/')


# # Edit Button - New Function.

# @login_required
# def edit_post(request, post_id):
#     post = Post.objects.get(id=post_id)

#     if request.method == "POST":
#         post.title = request.POST['title']
#         post.content = request.POST['content']
#         post.save()
#         return redirect('/')

#     return render(request, 'posts/edit_post.html', {'post': post})

# # For Regisering User.

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)   # auto login after register
#             return redirect('/')
#     else:
#         form = UserCreationForm()

#     return render(request, 'registration/register.html', {'form': form})


# # For Like / Unlike to Post.

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404
# from .models import Post, Like

# @login_required
# def toggle_like(request, post_id):
#     post = get_object_or_404(Post, id=post_id)

#     like, created = Like.objects.get_or_create(
#         post=post,
#         user=request.user
#     )

#     if not created:
#         # user already liked → unlike
#         like.delete()

#     return redirect('post_detail', post_id=post.id)

# # For Comment feature.

# from .forms import CommentForm
# from .models import Comment

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     comments = post.comments.all().order_by('-created_at')

#     if request.method == 'POST' and request.user.is_authenticated:
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.user = request.user
#             comment.save()
#             return redirect('post_detail', post_id=post.id)
#     else:
#         form = CommentForm()

#     context = {
#         'post': post,
#         'comments': comments,
#         'form': form
#     }
#     return render(request, 'posts/post_detail.html', context)


'''-------------------------------------------------------------------------------'''

#  Clean and easily readable logic as before.


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post, Like, Comment
from .forms import CommentForm


# Home page – list all posts
def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})


# Add new post – ONLY logged-in users
@login_required
def add_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return redirect('/')

    return render(request, 'posts/add_post.html')


# Edit post – ONLY the post owner
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('/')

    return render(request, 'posts/edit_post.html', {'post': post})


# Delete post – ONLY the post owner
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )
    post.delete()
    return redirect('/')


# Register user
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# Like / Unlike post
@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect('post_detail', post_id=post.id)


# Post detail + comments
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'posts/post_detail.html', context)
