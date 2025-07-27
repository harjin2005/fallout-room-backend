from rest_framework import serializers
from .models import Incident, Action, Deliverable

class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverable
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    deliverables = DeliverableSerializer(many=True, read_only=True)
    
    class Meta:
        model = Action
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Incident
        fields = '__all__'
