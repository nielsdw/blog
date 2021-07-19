from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs', views.blogs.as_view(), name='blogs'),
    path('blogs/<slug>', views.blogs.as_view(), name='slug')
]