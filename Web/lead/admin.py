from django.contrib import admin

from .models import lead, Comment, LeadFile

admin.site.register(lead)
admin.site.register(Comment)
admin.site.register(LeadFile)