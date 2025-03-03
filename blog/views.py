from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from blog.forms import BlogCreateForm
from django.contrib.auth.mixins import UserPassesTestMixin



# Create your views here.


class BlogCreateView(UserPassesTestMixin, CreateView):
    template_name = 'blog-create.html'
    form_class = BlogCreateForm # form
    success_url = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser