from django.shortcuts import render
from .models import Post , Categories , Coments , Likes , add_favorite



def post_list(request):

    post = Post.objects.filter(status = 'published')

    context = {
        "post" : post
        }

    return render(request , 'post/list.html' , context)

def post_detail(request , post_id):
    post = Post.objects.get(id=post_id)
    coments = post.coments_name.all()
    context = {
        "post" : post,
        "coments" : coments,
    }

    return render(request , "post/deatil.html" , context)
