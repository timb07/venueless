import uuid

from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    client_id = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    token_id = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    world = models.ForeignKey(to="World", db_index=True, on_delete=models.CASCADE)
    profile = JSONField()
    traits = ArrayField(models.CharField(max_length=200), blank=True)

    class Meta:
        unique_together = (("token_id", "world"), ("client_id", "world"))