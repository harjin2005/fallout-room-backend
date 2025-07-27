from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Incident, Action, Deliverable
from .serializers import IncidentSerializer, ActionSerializer, DeliverableSerializer
import random
from datetime import datetime
from django.http import JsonResponse
from django.core.management import call_command  

def setup_db(request):
    """One-time database setup"""
    try:
        call_command('migrate', '--run-syncdb')
        call_command('makemigrations', 'incident_response')
        call_command('migrate')
        return JsonResponse({"status": "Database setup complete - tables created"})
    except Exception as e:
        return JsonResponse({"error": f"Setup failed: {str(e)}"})



try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class DeliverableViewSet(viewsets.ModelViewSet):
    queryset = Deliverable.objects.all()
    serializer_class = DeliverableSerializer

# Add AI content generation as a separate function
@api_view(['POST'])
def generate_ai_content(request):
    """Generate AI content for empty deliverables"""
    
    if not OPENAI_AVAILABLE:
        return Response({"error": "OpenAI package not available"})
    
    try:
        # Find deliverables that need AI content
        empty_deliverables = Deliverable.objects.filter(content="")
        
        for deliverable in empty_deliverables:
            action = deliverable.action
            
            if action.ghostdraft:  # Only generate for GhostDraft actions
                ai_content = create_ai_content(action, deliverable)
                deliverable.content = f"🤖 OPENROUTER AI-GENERATED:\n\n{ai_content}"
                deliverable.save()
        
        return Response({"message": f"Generated AI content for {len(empty_deliverables)} deliverables"})
        
    except Exception as e:
        return Response({"error": str(e)})

def create_ai_content(action, deliverable):
    """Generate AI content using OpenRouter"""
    
    try:
        # Create OpenRouter client
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
            default_headers={
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Fallout Room Crisis Response System"
            }
        )
        
        # Create prompt based on action type
        action_type = action.title.lower()
        
        if 'customer' in action_type or 'notification' in action_type:
            prompt = f"""Create a professional customer breach notification for: {action.title}
Operator: {action.operator}
Format: {deliverable.deliverable_format}

Include: explanation of breach, affected information, protection measures, contact details.
Make it professional and reassuring for financial services customers."""
            
        elif 'regulatory' in action_type or 'compliance' in action_type:
            prompt = f"""Create a GDPR Article 33 regulatory notification for: {action.title}
Operator: {action.operator}
Format: {deliverable.deliverable_format}

Include: breach nature, affected data categories, consequences, remediation measures, DPO contact."""
            
        elif 'board' in action_type or 'executive' in action_type:
            prompt = f"""Create an executive board briefing for: {action.title}
Operator: {action.operator}
Format: {deliverable.deliverable_format}

Include: situation overview, business impact, board decisions required, strategic recommendations."""
            
        else:
            prompt = f"""Create a professional crisis response document for: {action.title}
Operator: {action.operator}
Description: {action.description}
Format: {deliverable.deliverable_format}

Provide actionable guidance for the assigned operator."""
        
        # Call OpenRouter API
        response = client.chat.completions.create(
            model="meta-llama/llama-3.2-3b-instruct:free",
            messages=[
                {"role": "system", "content": "You are a professional crisis management AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        # Fallback content
        return f"""Professional response document for: {action.title}

Assigned to: {action.operator}
Generated: {datetime.now().strftime('%B %d, %Y %H:%M:%S')}

OBJECTIVE: {action.description}

EXECUTION STEPS:
1. Review incident documentation and current status
2. Coordinate with incident response team
3. Execute assigned tasks per established procedures
4. Document all actions and decisions
5. Report status updates every 4 hours

This is a high-priority incident response task requiring immediate attention."""
