from django.contrib import admin
from .models import Conference, Submission, OrganisationCommittee
# Register your models here.
admin.site.register(Conference)
admin.site.register(Submission)
admin.site.register(OrganisationCommittee)
admin.site.site_title = "Gestion Conference IA"
admin.site.site_header = "Gestion Conference IA Admin"
admin.site.index_title = "Welcome Django App Conference"