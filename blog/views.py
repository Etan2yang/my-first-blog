from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    colors = [
        'red', 'orange', 'yellow','green'
    ]
    return render(request, 'blog/post_list.html', {'posts':posts, 'colors':colors})