from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

paths =[('Fullstack','Fullstack'),('Frontend', 'Frontend'),('Backend','Backend')]
status=[('Draft','Draft'),('Published','Published')]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(default='post.jpg', upload_to='profile_pics/cover/')
    category = models.CharField(max_length=20, choices=paths, default='fullstack')
    status =models.CharField(max_length=20, choices=status, default='draft')

    def __str__(self):
        return self.title

# Create your models here.
