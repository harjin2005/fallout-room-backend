from django.contrib import admin
from .models import Incident, Action, Deliverable

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['step', 'title', 'operator', 'is_complete', 'incident']
    list_filter = ['is_complete', 'ghostdraft']

@admin.register(Deliverable)
class DeliverableAdmin(admin.ModelAdmin):
    list_display = ['deliverable_format', 'voice_eligible', 'action']
    list_filter = ['deliverable_format', 'voice_eligible']
