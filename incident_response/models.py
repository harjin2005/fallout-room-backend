from django.db import models

class Incident(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Action(models.Model):
    incident = models.ForeignKey(Incident, related_name='actions', on_delete=models.CASCADE)
    step = models.IntegerField()
    title = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False)
    ghostdraft = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"Step {self.step}: {self.title}"

class Deliverable(models.Model):
    action = models.ForeignKey(Action, related_name='deliverables', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True, default="")
    deliverable_format = models.CharField(max_length=100)
    export_options = models.CharField(max_length=255)
    render_preview = models.BooleanField(default=False)
    voice_eligible = models.BooleanField(default=False)
    voice_transcript = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.deliverable_format} for {self.action.title}"
