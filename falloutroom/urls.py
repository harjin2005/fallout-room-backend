from django.contrib import admin  
from django.urls import path, include
from incident_response.views import setup_db

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('incident_response.urls')),
    path('setup-database/', setup_db, name='setup-database'),  # Direct access
]
