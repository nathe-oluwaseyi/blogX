from django.urls import path


from .views import (
    CategoryCreate, CategoryDelete, CategoryDetail, CategoryList,  CategoryUpdate, PostDelete, PostDetail, 
    PostList, PostUpdate, TagCreate, TagDelete, TagDetail, TagList, TagUpdate, PostCreate,
)

app_name = "blog"

urlpatterns = [
    path("post/create/", PostCreate.as_view(), name="post_create"),
    path("post/<int:year>/<int:month>/<slug:slug>/update/", PostUpdate.as_view(), name="blog_update"),
    path("post/<int:year>/<int:month>/<slug:slug>/delete/", PostDelete.as_view(), name="blog_delete"),
    path("", PostList.as_view(), name="blog_post_list"),
    path("post/<int:year>/<int:month>/<slug:slug>/", PostDetail.as_view(), name="blog_post_detail"),
    path("tag/create/", TagCreate.as_view(), name="tag_create"),
    path("tag/<slug:slug>/update/", TagUpdate.as_view(), name="tag_update"),
    path("tag/<slug:slug>/delete/", TagDelete.as_view(), name="tag_delete"),
    path("tag/", TagList.as_view(), name="blog_tag_list"),
    path("tag/<slug:slug>/", TagDetail.as_view(), name="blog_tag_detail"),
    path("category/create/", CategoryCreate.as_view(), name="category_create" ),
    path("category/<slug:slug>/update/", CategoryUpdate.as_view(), name="category_update"),
    path("category/<slug:slug>delete/", CategoryDelete.as_view(), name="category_delete"),
    path("category/", CategoryList.as_view(), name="blog_category_list"),
    path("category/<slug:slug>/", CategoryDetail.as_view(), name="blog_category_detail"),
    
]

