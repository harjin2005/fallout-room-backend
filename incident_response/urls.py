from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('incidents', views.IncidentViewSet)
router.register('actions', views.ActionViewSet)
router.register('deliverables', views.DeliverableViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate-ai/', views.generate_ai_content, name='generate-ai'),
]
