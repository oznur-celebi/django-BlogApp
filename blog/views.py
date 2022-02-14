from multiprocessing import context
from django.http import HttpResponseRedirect
# from urllib import response
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView, 
    FormView,
)
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required





def home(request):
    context = {
        'posts':  Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model =Post
    template_name ='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name ='posts'
    ordering =['-date_posted']



def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post_detail.html", {"post": post})
    
# def get_context_data(self, *args, **kwargs):
		
# 		stuff = get_object_or_404(Post, id=self.kwargs['id'])
# 		total_likes = stuff.total_likes()	
		
# 		liked = False
# 		if stuff.likes.filter(id=self.request.user.id).exists():
# 			liked = True

# 		context["total_likes"] = total_likes()
# 		context["liked"] = liked
# 		return context


def add_comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author =request.user
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})




# @login_required
# def add_comment(request, id):
#     post = Post.objects.get(id=id)
#     if request.method == 'POST':
#         c_form = CommentForm(request.POST, request.FILES)
#         if c_form.is_valid():
#             comment =request.POST.get('body')
#             comment=Comment.objects.create(post=post, author = request.user, content=)
#             comment.save()
#             redirect(post.get_absolute_url())
#         else:
#             c_form =CommentForm()
#             return render (request,'blog/post_detail.html', {"c_form": c_form})



    #  blog = Blog.objects.get(id=id)
    # form = BlogForm(instance=blog)
    # if request.method == "POST":
    #     form = BlogForm(request.POST, request.FILES, instance=blog)
    #     if form.is_valid():
    #         form.owner = request.user
    #         form.save()
    #         return redirect("home")

    # context = {
    #     "blog": blog,
    #     "form": form,
    # }
    # return render(request, "blog/post_update.html", context)


# class PostDisplayView(DetailView):
#      model =Post
#      template_name = 'post_detail.html'
#      context_object_name = 'post'

#      def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['comments'] = Comment.objects.filter(message=self.object)
#         context['form'] = CommentForm()
#         return context

# class PostComment(SingleObjectMixin, FormView):
#     model = Post
#     form_class = CommentForm
#     template_name = 'post_detail.html'
    
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().post(request, *args, **kwargs)

#     def get_form_kwargs(self):
#         kwargs = super(PostComment, self).get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs

#     def form_valid(self, form):
#         comment= form.save(commit=False)
#         comment.post = self.object
#         comment.save()
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         post = self.get_object()
#         return reverse('post_detail', kwargs={'pk': post.pk}) 



# class PostDetailView(View):

#     def get(self, request, *args, **kwargs):
#         view = PostDisplayView.as_view()
#         return view(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         view = PostComment.as_view()
#         return view(request, *args, **kwargs)



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content','date_posted','cover','category', 'status']
    
     
    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title', 'content','date_posted','cover','category', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model =Post
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



# def like_view(request, id):
#     post = Post.objects.get(id=id)
#     liked=False

#     if post.likes.filter(id=request.user.id).exists():
# 	    post.likes.remove(request.user)
# 	    liked = False
    
#      else:
# 	    post.likes.add(request.user)
# 		liked = True
         
#      return HttpResponseRedirect(reverse('post-detail', args=[str(id)]))