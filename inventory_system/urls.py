from django.contrib import admin
from django.urls import path, include  # Import include to reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('', include('inventory.urls')),  # Include the URLs from the inventory app
]
