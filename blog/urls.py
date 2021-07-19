from django.urls import path

from blog import views

urlpatterns = [
    path("blogs", views.Blogs.as_view(), name="blogs"),
    path("blogs/<slug>", views.Blogs.as_view(), name="slug"),
]
