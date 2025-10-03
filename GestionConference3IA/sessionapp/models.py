from django.db import models
from conferenceapp.models import Conference

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)    
    session_date = models.DateField()
    start_time = models.TimeField()   
    end_time = models.TimeField()
    room = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #conference = models.ForeignKey("conferenceapp.Conference", on_delete=models.CASCADE related_name='sessions')
    confereence = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='sessions')