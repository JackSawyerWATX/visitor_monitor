#visitor_counter/urls.py
from django.contrib import admin
from django.urls import path, include
from visitor_counter.views import visitor_count, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Use the new home view for the empty path
    path('visitor_count/home.html', visitor_count, name='visitor_count/home.html'),
]