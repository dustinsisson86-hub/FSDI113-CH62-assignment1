from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Status
from django.contrib.auth.models import User
# Create your views here.

# List view for displaying all posts
class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "post"
    published_status = Status.objects.get(name="Published")

    # Override get_queryset to filter posts by published status
    queryset = Post.objects.filter(status=published_status).order_by("-created_on").reverse()
    

# Detail view for displaying a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    


# Create view for creating a new post
class PostCreateView(CreateView):
    model = Post
    template_name = "posts/post_new.html"
    fields = ['title', 'subtitle','body']

    def form_valid(self, form):
        print(User.objects.all())
        form.instance.author = User.objects.last()
        return super().form_valid(form)
    

  # Update view for editing an existing post  
class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    fields = ['title', 'subtitle','body']


# Delete view for deleting a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = "/posts/"


#List view for displaying all draft posts
class PostDraftListView(ListView):
    model = Post
    template_name = "posts/draft_list.html"
    context_object_name = "post"
    
    def get_queryset(self):
        return Post.objects.filter(status__name="Draft").order_by("-created_on")

#List view for displaying only archived posts
class PostArchivedListView(ListView):
    model = Post
    template_name = "posts/archived_list.html"
    context_object_name = "post"
    
    def get_queryset(self):
        return Post.objects.filter(status__name="Archived").order_by("-created_on")