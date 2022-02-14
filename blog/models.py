
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

 

paths =[('Fullstack','Fullstack'),('Frontend', 'Frontend'),('Backend','Backend')]
status=[('Draft','Draft'),('Published','Published')]

class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag =models.CharField(max_length=100,null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,  related_name="author")
    cover = models.ImageField(default='post.jpg', upload_to='profile_pics/cover/')
    category = models.CharField(max_length=20, choices=paths, default='fullstack')
    status =models.CharField(max_length=20, choices=status, default='draft')
    liked =models.ManyToManyField(User, related_name="liked")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse(
        # )
         return reverse('blog-home')

    @property
    def number_likes(self):
        return self.liked.all().count()


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
 
   

    def __str__(self):
        return 'Comment {} by {} on {}'.format(self.body, self.author, self.created) 


LIKE_CHOICES ={
    ('Like','Like'),
    ('Unlike', 'Unlike'),
}

class Like(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE , related_name='user_Like')
    post= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_like')
    value =models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)


    
    def __str__(self):
        return str(self.post)
    