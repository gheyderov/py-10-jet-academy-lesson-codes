from django.urls import path
from blog.views import BlogCreateView


urlpatterns = [
    path('blog-create/', BlogCreateView.as_view(), name = 'blog-create')
]