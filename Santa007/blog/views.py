
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Post


# Class Based Views

# Create view class (create new post)
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"

# list post views
class PostListView(ListView):
    model = Post 
    template_name = "blog/post_list.html"

# detail post views
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

# update post views
class PostUpdateView(UpdateView):
    model = Post
    fields = [
        'title',
         'body'
    ]
    template_name = "blog/post_form.html"
    success_url: reverse_lazy('blog:all')

# delete post views
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('blog:all')