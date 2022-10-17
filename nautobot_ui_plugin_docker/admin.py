from django.contrib import admin
from .models import NautobotSavedTopology


@admin.register(NautobotSavedTopology)
class NautobotSavedTopologyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "timestamp", "topology",)
