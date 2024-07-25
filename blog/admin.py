from django.contrib import admin
from .models import Post , Categories , Coments , Likes , add_favorite 

admin.site.register(add_favorite)
admin.site.register(Likes)
admin.site.register(Coments)
admin.site.register(Categories)
admin.site.register(Post)

