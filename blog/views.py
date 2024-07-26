from django.shortcuts import render
from .models import Post , Categories , Coments , Likes , add_favorite
from django.contrib.auth.decorators import login_required

def post_list(request):

    post = Post.objects.filter(status = 'published')

    context = {
        "post" : post
        }

    return render(request , 'post/list.html' , context)

def post_detail(request , post_id):
    post = Post.objects.get(id=post_id)
    coments = post.coments_name.all()

    like_counter = post.post_likes.count()

    context = {
        "post" : post,
        "coments" : coments,
        "likes" : like_counter
    }

    return render(request , "post/deatil.html" , context)


def categories_list(request):
    category = Categories.objects.all()
    
    context = {
        "category" : category
    }

    return render(request , "post/category.html" , context)


def categories_detail(request , cat_id):
    category = Categories.objects.get(id=cat_id)
    posts = category.posts.filter(status = 'published')
    context = {
        "detail" : category,
        "posts" : posts
        
    }

    return render(request , "post/category_detail.html" , context)


@login_required
def favorite_posts(request):
    
    favorite_posts = add_favorite.objects.filter(user=request.user).values_list('post', flat=True)
    posts = Post.objects.filter(id__in=favorite_posts, status=Post.PUBLISHED)
    
    context = {
        'posts': posts
    }
    
    return render(request, 'post/favorite.html', context)