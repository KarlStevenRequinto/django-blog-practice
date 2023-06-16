# register urls here
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.starting_page, name="starting-page"),  # starting page functional view
    path("",views.StartingPageView.as_view(),name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"), # dynamic segment (/posts/my-first-post)
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]
