from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 1 or value > 5 :
        raise ValidationError('rating moust be between 1 and 5 ')

class Categories(models.Model):
    category = models.CharField(max_length=100)
    bio = models.TextField()
    parents = models.ForeignKey('self' ,on_delete=models.CASCADE ,related_name='children' , blank=True , null=True)

    def __str__(self):
        return self.category

class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media/post')
    body = models.TextField()
    creat_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )
    author = models.ForeignKey(User , on_delete= models.CASCADE)
    category = models.ForeignKey(Categories , related_name='posts' , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Coments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="coments_name" )
    coment_authors = models.ForeignKey(User , on_delete= models.CASCADE)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add= True)
    parents = models.ForeignKey('self' ,on_delete=models.CASCADE ,related_name='children' , blank=True , null=True)
    rating = models.PositiveSmallIntegerField(validators=[validate_rating])

    def __str__(self):
        return f"{self.post.title} - coments"

class Likes(models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE , related_name='post_likes')
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class add_favorite(models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE , related_name="favorite_post")
    user = models.ForeignKey(User , on_delete=models.CASCADE)




