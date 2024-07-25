from django.urls import path
from . import views
urlpatterns = [
    path('' , views.post_list , name="list" ),
    path('<int:post_id>/' , views.post_detail , name="detail" )
]
