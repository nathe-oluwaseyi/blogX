from django.urls import path


from .views import CategoryDetail, CategoryList, PostDetail, PostList, TagDetail, TagList

app_name = "blog"
urlpatterns = [
    path("", PostList.as_view(), name="blog_post_list"),
    path("post/<int:year>/<int:month>/<slug:slug>/", PostDetail.as_view(), name="blog_post_detail"),
    path("tag", TagList.as_view(), name="blog_tag_list"),
    path("tag/<slug:slug>/", TagDetail.as_view(), name="blog_tag_detail"),
    path("category", CategoryList.as_view(), name="blog_category_list"),
    path("category/<slug:slug>/", CategoryDetail.as_view(), name="blog_category_detail")
    
]

