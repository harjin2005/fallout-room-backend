from rest_framework import routers
from django.urls import path, include
from .views import IncidentViewSet, ActionViewSet, DeliverableViewSet

router = routers.DefaultRouter()
router.register(r'incidents', IncidentViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'deliverables', DeliverableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
