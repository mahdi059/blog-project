from django.urls import path
from . import views
urlpatterns = [
    path('' , views.post_list , name="list" ),
    path('category/' , views.categories_list , name="category_list" ),
    path('<int:post_id>/' , views.post_detail , name="detail" ),
    path('cat/<int:cat_id>/' , views.categories_detail , name="category_detail" ),
    
]
