from django.urls import path
from . import views
urlpatterns = [
    path('posts' , views.post_list , name="list" ),
    path('category/' , views.categories_list , name="category_list" ),
    path('post/<int:post_id>/' , views.post_detail , name="detail" ),
    path('cat/<int:cat_id>/' , views.categories_detail , name="category_detail" ),
    path('favorite/' , views.favorite_posts , name="favorite_post"),
    path('' , views.home , name="home")
    
]