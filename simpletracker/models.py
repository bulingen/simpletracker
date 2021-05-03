from django.db import models


class LogEntry(models.Model):
    created_at = models.DateTimeField(null=False, blank=False)
    visitor_id = models.CharField(null=False, blank=False, max_length=255)
    page = models.CharField(null=False, blank=False, max_length=255)
