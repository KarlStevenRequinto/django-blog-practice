# register urls here
from django.urls import path
from . import views
urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # starting page
    path("posts", views.posts, name="posts-page"), # dynamic segment (/posts/my-first-post)
    path("posts/<slug>", views.post_detail, name="post-detail-page")
]
