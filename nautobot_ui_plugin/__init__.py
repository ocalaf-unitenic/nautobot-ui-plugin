from nautobot.extras.plugins import PluginConfig

class NautobotUIConfig(PluginConfig):
    name = 'nautobot_ui_plugin'
    verbose_name = 'Nautobot UI'
    description = 'A topology visualization plugin for Nautobot powered by NextUI Toolkit.'
    version = '0.10.4'
    author = 'Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen'
    author_email = 'netzadmin@gwdg.de'
    base_url = 'nautobot-ui'
    required_settings = []
    default_settings = {}
    caching_config = {
        '*': None
    }

config = NautobotUIConfig
