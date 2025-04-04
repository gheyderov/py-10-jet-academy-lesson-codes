from django.urls import path
from core.views import home, ContactView, about, export_view

urlpatterns = [
    path('', home, name = 'home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', about, name = 'about'),
    path('export/', export_view, name = 'export')
]
