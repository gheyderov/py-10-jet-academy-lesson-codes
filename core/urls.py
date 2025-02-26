from django.urls import path
from core.views import home, ContactView, about

urlpatterns = [
    path('', home, name = 'home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about', about, name = 'about')
]
