from django.shortcuts import redirect


def redirect_root(request):
    return redirect('blog:blog_post_list') # redirect to the given url pattern name