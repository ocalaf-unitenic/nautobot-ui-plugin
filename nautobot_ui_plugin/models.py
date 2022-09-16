from django.db import models
from nautobot.core.models import BaseModel
from nautobot.utilities.querysets import RestrictedQuerySet


class NautobotSavedTopology(BaseModel):

    name = models.CharField(max_length=100, blank=True)
    topology = models.JSONField()
    layout_context = models.JSONField(null=True, blank=True)
    created_by = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    timestamp = models.DateTimeField()

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return str(self.name)
