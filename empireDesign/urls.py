from django.urls import path

from . import views

urlpatterns = [
    path('', views.intro, name="index"),
    path("index", views.index, name="a"),
    path("about", views.about, name="about"),
    path("what-you-need", views.what_you_need, name="what-you-need"),
    path("contact-us/store", views.contact_us_req, name="contact-us-req"),
    path("posts/", views.get_all_posts, name="get_all_posts"),
    path("contact-us/<type>", views.contact_us, name="contact-us"),
    path('post/<name>', views.PostDetails, name="postDetails"),
]