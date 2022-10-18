from nautobot.extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:nautobot_ui_plugin_docker:topology",
        link_text="Topology Viewer",
        buttons=(),
        permissions=["nautobot_ui_plugin_docker.view_topology"],
    ),
)