from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

 

paths =[('Fullstack','Fullstack'),('Frontend', 'Frontend'),('Backend','Backend')]
status=[('Draft','Draft'),('Published','Published')]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,)
    cover = models.ImageField(default='post.jpg', upload_to='profile_pics/cover/')
    category = models.CharField(max_length=20, choices=paths, default='fullstack')
    status =models.CharField(max_length=20, choices=status, default='draft')
    # likes =models.ManyToManyField(User, related_name="liked")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post-detail', kwargs={'pk': self.pk})
         return reverse('blog-home')



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
 
    # @property
    # def number_of_comments(self):
    #     return Comment.objects.filter(blogpost_connected=self).count()

    def __str__(self):
        return 'Comment {} by {} on {}'.format(self.body, self.author, self.created) 