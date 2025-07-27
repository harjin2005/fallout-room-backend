from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from incident_response.views import simple_setup




router = DefaultRouter()
router.register('incidents', views.IncidentViewSet)
router.register('actions', views.ActionViewSet)
router.register('deliverables', views.DeliverableViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('incident_response.urls')),
    path('setup/', simple_setup, name='simple-setup'),
]