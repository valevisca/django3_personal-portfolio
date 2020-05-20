from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    # We pull out all the blogs from the Db
    
    #blogs = Blog.objects.all()
    
    # An alternative when we have many ojects in the database is to retrieve
    # a subset only. THis is an example using '.order_by()'. Negative date means
    # the most recent ones. 
    # If we then add [:3] we can filter only 3 elements
    blogs = Blog.objects.order_by('-date')
    # And we then pass it as a dictionary to 'render'
    # Study note: we will then need to go to the template (html page)
    # so to use and visualize blogs which we are passing below...
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    # We used the 'get_object_or_404' method we imported to retrieve from the object
    # 'Blog' the instance wiht 'pk' (primary key in Db terminology) equal to the
    # blog_id
    blog = get_object_or_404(Blog, pk=blog_id)
    # We then pass it via render to the proper template
    return render(request, 'blog/detail.html', {'blog': blog})