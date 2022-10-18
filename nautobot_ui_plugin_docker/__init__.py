from nautobot.extras.plugins import PluginConfig

class NautobotUIConfig(PluginConfig):
    name = 'nautobot_ui_plugin_docker'
    verbose_name = 'Nautobot UI Docker'
    description = 'A topology visualization plugin for Nautobot powered by NextUI Toolkit.'
    version = '0.10.15'
    author = 'Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen'
    author_email = 'netzadmin@gwdg.de'
    base_url = 'nautobot-ui-docker'
    required_settings = []
    default_settings = {}
    caching_config = {
        '*': None
    }

config = NautobotUIConfig
