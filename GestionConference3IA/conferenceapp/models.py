from django.db import models
from userapp.models import User
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
def clean(self):
    if  self.date_debut > self.date_fin:
        raise ValidationError("End date cannot be earlier than start date.")
    
class Conference(models.Model):
    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    THEME_CHOICES = [
        ("AI", "Artificial Intelligence"),
        ("ML", "Machine Learning"),
        ("DS", "Data Science"),
        ("CV", "Computer Vision"),
        ("NLP", "Natural Language Processing"),
    ]
    theme = models.CharField(max_length=255, choices=THEME_CHOICES)
    location = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField(
    validators=[MinLengthValidator(30, message="La description doit contenir au moins 30 caracteres.")]
)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
        
class Submission(models.Model):
    submission_id = models.CharField(max_length=255, primary_key=True, unique=True)
    title = models.CharField(max_length=50)
    abstract = models.TextField()
    keywords = models.TextField()
    paper = models.FileField(upload_to='papers/')
    STATUS_CHOICES = [
        ("submitted", "submitted"),
        ("under review", "under review"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    submission_date = models.DateTimeField(auto_now_add=True)
    payed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='submissions')
    user =models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')


class OrganisationCommittee(models.Model):
    committee_id = models.CharField(max_length=255, primary_key=True, unique=True)
    
    ROLE_CHOICES = [
        ("chair", "chair"),
        ("co-chair", "co-chair"),
        ("member", "member"),
    ]
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='committees')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='committees')