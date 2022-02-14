from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post,Comment, Like

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)