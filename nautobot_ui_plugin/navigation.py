from nautobot.extras.plugins import PluginMenuItem


menu_items = (
    PluginMenuItem(
        link="plugins:nautobot_ui_plugin:topology",
        link_text="Topology Viewer",
        permissions=["nautobot_ui_plugin.view_topology"],
        buttons=(),
    ),
)