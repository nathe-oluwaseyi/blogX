from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from .models import Category, Post, Tag
from .forms import TagForm, PostForm, CategoryForm
from.utils import ObjectCreateMixin


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
    

class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'blog/tag_form.html'
      

class PostCreate(ObjectCreateMixin, View):
    form_class = PostForm
    template_name = 'blog/post_form.html'
      

class CategoryCreate(ObjectCreateMixin, View):
    form_class = CategoryForm
    template_name = 'blog/category_form.html'
    
    
class TagUpdate(View):
    form_class = TagForm
    template_name = 'blog/tag_form_update.html'
    model = Tag
    
    def get(self, request, slug):
        tag = get_object_or_404(self.model, slug__iexact=slug)
        context = {'form': self.form_class(instance=tag), 'tag': tag}
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        tag = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=tag)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        else:
            context = {'form': self.form_class(request.POST), 'tag': tag}
            return render(request, self.template_name, context)


class PostUpdate(View):
    form_class = PostForm
    template_name = 'blog/post_form_update.html'
    model = Post
    
    def get(self, request, year, month, slug):
        post = get_object_or_404(
            self.model, published_at__year=year, published_at__month=month, slug=slug)
        context = {'form': self.form_class(instance=post), 'post': post}
        return render(request, self.template_name, context)
    
    def post(self, request, year, month, slug):
        post = get_object_or_404(
            self.model, published_at__year=year, published_at__month=month, slug=slug
        )
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {'form': self.form_class(request.POST), 'post': post}
            return render(request, self.template_name, context)
    
    
class CategoryUpdate(View):
    form_class = CategoryForm
    model = Category
    template_name = 'blog/category_form_update.html'
    
    def get(self, request, slug):
        category = get_object_or_404(self.model, slug__iexact=slug)
        context = {'form': self.form_class(instance=category), 'category': category}
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        category = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=category)
        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        else:
            context = {'form': self.form_class(request.POST), 'category': category}
            return render(request, self.template_name, context)
        

class TagDelete(View):
    model = Tag
    template_name = 'blog/tag_confirm_delete.html'
    
    def get(self, request, slug):
        tag = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template_name, {'tag': tag})
    
    def post(self, request, slug):
        tag = get_object_or_404(self.model, slug__iexact=slug)
        tag.delete()
        return redirect('blog:tag_list')
    

class PostDelete(View):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    
    def get(self, request, year, month, slug):
        post = get_object_or_404(
            self.model, published_at__year=year, published_at__month=month, slug=slug)
        return render(request, self.template_name, {'post': post})
    
    def post(self, request, year, month, slug):
        post = get_object_or_404(
            self.model, published_at__year=year, published_at__month=month, slug=slug)
        post.delete()
        return redirect('blog:blog_post_list')
    
    
class CategoryDelete(View):
    model = Category
    template_name = 'blog/category_confirm_delete.html'
    
    def get(self, request, slug):
        category = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template_name, {'category': category})
    
    def post(self, request, slug):
        category = get_object_or_404(self.model, slug__iexact=slug)
        category.delete()
        return redirect('blog:category_list')