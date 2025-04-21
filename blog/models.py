from django.db import models
from django.utils.text import slugify
from datetime import date
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, help_text='A label for URL config', unique_for_month='published_at')
    content = models.TextField()
    #author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="posts")
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    featured_image = models.ImageField(upload_to="post/", blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    read_time = models.PositiveIntegerField(default=0) # Estimate read time in minutes
    
    class Meta:
        verbose_name = 'blog post'
        ordering = ['-published_at', 'title']
        get_latest_by = 'published_at'
        
    
    '''def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)'''

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:blog_post_detail', 
                       kwargs={'year': self.published_at.year,
                               'month': self.published_at.month,
                               'slug': self.slug})
        
    
    
'''class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="authors/", blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username'''
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ['name']

    '''def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)'''

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:blog_category_detail', kwargs={'slug': self.slug})

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ['name']

    '''def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)'''

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:blog_tag_detail', kwargs={'slug': self.slug})
    
    
'''class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"'''



'''class Interaction(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="interaction")
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Interactions for {self.post.title}" '''