from rest_framework.routers import APIRootView
from rest_framework.viewsets import ModelViewSet
from nautobot_ui_plugin_docker.models import NautobotSavedTopology
from . import serializers


class NautobotUIPluginRootView(APIRootView):
    """
    NautobotUI_plugin API root view
    """
    def get_view_name(self):
        return 'NautobotUI'


class NautobotSavedTopologyViewSet(ModelViewSet):
    queryset = NautobotSavedTopology.objects.all()
    serializer_class = serializers.NautobotSavedTopologySerializer
