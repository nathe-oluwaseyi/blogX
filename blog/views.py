from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import Category, Post, Tag


class PostList(View):
    template_name = 'blog/post_list.html'
    
    def get(self, request):
        post_list = Post.objects.all() # define the data to be displayed on the webpage
        context = {'post_list': post_list}
        return render(request, self.template_name, context)  

class PostDetail(View):
    template_name = 'blog/post_detail.html'
    
    def get(self, request, year, month, slug):
        post = get_object_or_404(Post, published_at__year=year, published_at__month=month, slug=slug)
        context = {'post': post}
        return render(request, self.template_name, context )
    

class TagList(View):
    template_name = 'blog/tag_list.html'
    
    def get(self, request):
        tag_list = Tag.objects.all()
        context = {"tag_list": tag_list}
        return render(request, self.template_name, context)
    

class TagDetail(View):
    template_name = 'blog/tag_detail.html'
    
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug=slug)
        context = {"tag": tag}
        return render(request, self.template_name, context)
    
    
class CategoryList(View):
    template_name = 'blog/category_list.html'
    
    def get(self, request):
        category_list = Category.objects.all()
        context = {"category_list": category_list}
        return render(request, self.template_name, context)
    
    
class CategoryDetail(View):
    template_name = 'blog/category_detail.html'
    
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        context = {"category": category}
        return render(request, self.template_name, context)