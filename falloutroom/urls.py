from django.contrib import admin
from django.urls import path, include
from incident_response.views import simple_setup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('incident_response.urls')),
    path('setup/', simple_setup, name='simple-setup'),
]
