from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("post",views.latest_posts,name="posts"),
    path("post/<slug:slug>",views.pData,name="postdetail"),#<slug:slug>
]

