
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('help/', include('home.urls')),
    path('view-request/', include('home.urls')),
    path('help_req/', include('home.urls')),
]
