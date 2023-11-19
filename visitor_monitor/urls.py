# visitor_monitor/urls.py
from django.contrib import admin
from django.urls import path, include
from visitor_counter.views import visitor_count, home, reset_count

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    path('visitor_count/', visitor_count, name='visitor_count'),
    path('reset_count/', reset_count, name='reset_count'),
]
