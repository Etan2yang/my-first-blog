from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    # colors = '0 1 2 3'
    # c2 = '10 12 14 55'
    return render(request, 'blog/post_list.html', {'posts':posts})