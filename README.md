# Nautobot UI Plugin

A topology visualization plugin for [Nautobot](https://github.com/nautobot/nautobot) powered by [NextUI](https://developer.cisco.com/site/neXt/) Toolkit. Tested with Nautobot 1.1.5.

# Installation

General installation steps and considerations follow the [official guidelines](https://netbox.readthedocs.io/en/stable/plugins/).

### Package Installation from PyPi

Assuming you use a Virtual Environment for Nautobot:
```
$ source /opt/netbox/venv/bin/activate
(venv) $ pip3 install nautobot-ui-plugin
```

### Package Installation from Source Code
The source code is available on [GitHub](https://github.com/iDebugAll/nextbox-ui-plugin).<br/>
Download and install the package. Assuming you use a Virtual Environment for Nautobot:
```
$ git clone https://github.com/ocalaf-unitenic/nautobot-ui-plugin/nautobot-ui-plugin
$ cd nautobot-ui-plugin
$ source /opt/netbox/venv/bin/activate
(venv) $ pip3 install .
```

To ensure NextBox UI plugin is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the NetBox root directory (alongside `requirements.txt`) and list the `nautobot-ui-plugin` package:

```no-highlight
# echo nautobot-ui-plugin >> local_requirements.txt
```

### Enable the Plugin
In a global Netbox **configuration.py** configuration file, update or add PLUGINS parameter:
```python
PLUGINS = [
    'nautobot_ui_plugin_docker',
]
```

Optionally, update a PLUGINS_CONFIG parameter in **configuration.py** to rewrite default plugin behavior:
```python
#PLUGINS_CONFIG = {
#    'nautobot_ui_plugin_docker': {
#        'layers_sort_order': (
#            ADD YOUR SETTINGS HERE
#            layer_sort_order is a tuple
#        ),
#        'icon_model_map': {
#            ADD YOUR SETTINGS HERE
#            icon_model_map is a dict
#        },
#        'icon_role_map': {
#            ADD YOUR SETTINGS HERE
#            icon_role_map is a dict
#        }
#        'undisplayed_device_role_slugs': (
# #          ADD YOUR SETTINGS HERE
#            undisplayed_device_role_slugs value is a list or a tuple
#            Listed device role slugs are hidden on initial view load,
#            you may then hide/display any layer with a control button.
#        ),
#        'undisplayed_device_tags': (
#           ADD YOUR SETTINGS HERE
#           undisplayed_device_tags value is a list or a tuple of regex strings.
#           Devices with tags matching any of listed regular expressions are hidden
#           on initial view load, you may then hide/display any layer with a control button.
#        ),
#        'select_layers_list_include_device_tags': (
#           ADD YOUR SETTINGS HERE
#           select_layers_list_include_device_tags value is a list or a tuple of regex strings.
#           Use this parameter to control tags listed in Select Layers menu.
#           If specified, it works as allow list.
#        ),
#        'select_layers_list_exclude_device_tags': (
#           ADD YOUR SETTINGS HERE
#           select_layers_list_exclude_device_tags value is a list or a tuple of regex strings.
#           Use this parameter to control tags listed in Select Layers menu.
#           If specified, it filters out matched tags from the list, except ones mathcing 'undisplayed_device_tags'.
#        ),
#        'DISPLAY_PASSIVE_DEVICES': True|False,
#        'DISPLAY_LOGICAL_MULTICABLE_LINKS': True|False,
#        'DISPLAY_UNCONNECTED': True|False,
#        'INITIAL_LAYOUT': 'vertical'|'horizontal'|'auto'
#    }
#}
```
By default, the Plugin orders devices on a visualized topology based their roles in Netbox device attributes.<br/> This order may be controlled by 'layers_sort_order' parameter. Default sort order includes most commonly used naming conventions:
```
(
    'undefined',
    'outside',
    'border',
    'edge',
    'edge-switch',
    'edge-router',
    'core',
    'core-router',
    'core-switch',
    'distribution',
    'distribution-router',
    'distribution-switch',
    'leaf',
    'spine',
    'access',
    'access-switch',
)
```

By default, the Plugin automatically tries to identify the device icon type based on following logic:
1. 'icon_{icon_type}' tag in the Nautobot Device tags.
   Assign a tag to the device to manually control the displayed icon type (e.g. 'icon_router' or 'icon_switch').
   Supported icon types:
```
{
    'switch',
    'router',
    'firewall',
    'wlc',
    'unknown',
    'server',
    'phone',
    'nexus5000',
    'ipphone',
    'host',
    'camera',
    'accesspoint',
    'groups',
    'groupm',
    'groupl',
    'cloud',
    'unlinked',
    'hostgroup',
    'wirelesshost',
}
```
2. If no valid 'icon_{icon_type}' tags found, the Plugin checks the default icon to device_type mapping. You can control this behavior with 'icon_model_map' dict. The Plugin checks for substring in a full device_type attribute. Default mapping:

```
{
    'CSR1000V': 'router',
    'Nexus': 'switch',
    'IOSXRv': 'router',
    'IOSv': 'switch',
    '2901': 'router',
    '2911': 'router',
    '2921': 'router',
    '2951': 'router',
    '4321': 'router',
    '4331': 'router',
    '4351': 'router',
    '4421': 'router',
    '4431': 'router',
    '4451': 'router',
    '2960': 'switch',
    '3750': 'switch',
    '3850': 'switch',
    'ASA': 'firewall',
}
```
Keys are searched substrings. Values should be valid icon types as listed above.<br/>

3. If no match found on steps 1-2, the Plugin checks the Device Role slug to Icon mapping.<br/>
This mapping may be defined within 'icon_role_map' dict in Plugin parameters.<br/>
Default mapping already contains some general categories:
```
{
    'border': 'router',
    'edge-switch': 'switch',
    'edge-router': 'router',
    'core-router': 'router',
    'core-switch': 'switch',
    'distribution': 'switch',
    'distribution-router': 'router',
    'distribution-switch': 'switch',
    'leaf': 'switch',
    'spine': 'switch',
    'access': 'switch',
    'access-switch': 'switch',
}
```

4. Default value is 'unknown' (renders as a question mark icon).
<br/><br/>

The Plugin can control the visibility of the layers and/or specific nodes on the topology view.<br/>
The visibility control is currently implemented for specific device roles, device tags, unconnected devices, and passive devices:<br/>

  - Initial visibility behavior for specific device roles is controlled by 'undisplayed_device_role_slugs' plugin parameter. Listed device role slugs are hidden on initial view load, you may then hide/display any layer with a control button on the topology view page.<br/>

  - Initial visibility behavior for specific device tags is controlled by 'undisplayed_device_tags' plugin parameter. Devices with tags matching listed tag regular expressions are hidden on initial view load, you may then hide/display any layer with a control button on the topology view page.<br/>
  By default, the plugin lists all discovered device tags in Select Layers menu. You can use 'select_layers_list_include_device_tags' and 'select_layers_list_exclude_device_tags' plugin parameters to filter the included tags.<br/>
  All three tag visibility control parameters are optional lists of regular expressions. Tags matching 'undisplayed_device_tags' are always listed in Select Layers menu. Empty or unset 'select_layers_list_include_device_tags' allows all discovered tags to be listed in Select layers menu. If set, 'select_layers_list_include_device_tags' works as an allow list for matched tags. 'select_layers_list_exclude_device_tags' filters out matched tags from the list, excpept for ones matching 'undisplayed_device_tags'.

  - Initial visibility behavior for unconnected nodes is controlled by DISPLAY_UNCONNECTED boolean plugin parameter.<br/>
  By default, unconnected nodes are being displayed. Set DISPLAY_UNCONNECTED to False to hide them on initial topology view load.<br/>
  A separate 'Hide/Display Unconnected' button may then be used to hide or display those nodes.

  - Initial visibility for passive devices (patch panels, PDUs) is controlled by DISPLAY_PASSIVE_DEVICES boolean plugin parameter. A device is considered passive if it has cables connected to Front and Rear Ports only and not to Interfaces.<br/>Passive devices are hidden by default. You can display them with 'Display Passive Devices' button on the topology view page. <br/>
  Actual multi-cable connections between the end-devices a replaced by the direct logical connection once the passive devices are hidden. This logical direct link may be displayed regardless of the passive device visibility in addition to the cabling across patch panels if you set DISPLAY_LOGICAL_MULTICABLE_LINKS plugin parameter to True. DISPLAY_LOGICAL_MULTICABLE_LINKS is set to False by default. This parameter only affects the initial logical link visibility. With hidden passive devices, it is always being displayed.<br/>
<br/>

Device layers are ordered automatically by default. You can control this behavior with INITIAL_LAYOUT plugin parameter. Valid options are 'vertical', 'horizontal', and 'auto'.<br/>
'auto' layout relies on NeXt UI dataprocessor best-effort algorithms. It spreads the Nodes across the view so they would be as distant from each other as possible. You may use it if the vertical and horizontal initial layout does not work properly in your browser (this is the issue to be fixed).



### Collect Static Files
The Plugin contains static files for topology visualization. They should be served directly by the HTTP frontend. In order to collect them from the package to the Netbox static root directory use the following command:
```
(venv) $ cd /opt/netbox/netbox/
(venv) $ python3 manage.py collectstatic
```

### Apply Database Migrations

> For plugin version 0.8.0 and above.

Apply database migrations with Django `manage.py`:
```
(venv) $ python3 manage.py migrate
```

### Restart Netbox
Restart the WSGI service to apply changes:
```
sudo systemctl restart netbox
```

# Installation with Docker
The Plugin may be installed in a Netbox Docker deployment. 
The package contains a Dockerfile for [Netbox-Community Docker](https://github.com/netbox-community/netbox-docker) extension. Latest-LDAP version is used by default as a source.<br/>
Download the Plugin and build from the source:
```
$ git clone https://github.com/ocalaf-unitenic/nautobot-ui-plugin/
$ cd nautobot-ui-plugin
$ docker build -t netbox-custom .
```
Update a netbox image name in **docker-compose.yml** in a Netbox Community Docker project root:
```yaml
services:
  netbox: &netbox
    image: netbox-custom:latest
```
Update a **configuration.py**. It is stored in netbox-docker/configuration/ by default. Update or add PLUGINS parameter and PLUGINS_CONFIG parameter as described above.

Rebuild the running docker containers:
```
$ cd nautobot-compose-docker
$ docker-compose down
$ docker-compose up -d
```
Nautobot Community Docker setup performs static file collection and database migrations on every startup. No manual actions are required.

# Fixing Common Installation and Post-Upgrade Issues

If you are experiencing some unexpected errors or visual behaviors after the installation or upgrade, please make sure that you execute the following steps first:

1. Clear your browser cache and reload the page.
2. Re-collect static files: `(venv) $ python3 manage.py collectstatic --clear`.
3. Re-apply database migrations: `(venv) $ python3 manage.py migrate`.

# Usage

Once installed and initialized, the Plugin runs on a backend.<br/>
The Plugin supports a topology visualization of arbitrary sets of Sites and Regions.<br/>
<br/>
You can access Topology visualizations in different ways:
1. By clicking a custom plugin Topology button on a Site page.
![](samples/sample_topology_button.png)
The Site topology visualization will open in a pop-up window:
![](samples/sample_topology_view.png)<br/>
Nodes are draggable and clickable:
![](samples/sample_node_tooltip_content.png)<br/>
You can switch between vertical and horizontal layers sort order back and forth. Default is vertical.<br/>

2. Using Plugins dropdown menu item: *Plugins -> NextBox UI -> Topology Viewer*.<br/>
Use Search form controls to pick desired Sites, Regions, or Devices.<br/>
![](samples/sample_topology_viewer_page01.png)
<br/>

### Visibility control

You can display or hide any specific device roles on the topology view with 'Select Layer' button:
![](samples/sample_layer_visibility.png)<br/>
The list of available device roles is generated automatically based on discovered devices for a visualized site.<br/>
<br/>
'Display/Hide Unconnected' button hides or displays the devices with no links attached.<br/>
<br/>
'Display/Hide Passive Devices' buttons hides or displays the passive devices (patch pannels, PDUs, etc).<br/>
<br/>
In a samples below, edge-sw01 is connected with core-rtr01 and core-rtr02 through Patch Panel A and Patch Panel B with multiple cable hops:<br/>
![](samples/sample_patch_panels.png)<br/>
Once you hide the passive devices (default state), a logical direct link shows up between the edge switch and the core routers:<br/>
![](samples/sample_hide_passive.png)<br/>
If DISPLAY_LOGICAL_MULTICABLE_LINKS is set to True (default is False) this logical link is displayed initially:<br/>
![](samples/sample_display_logical_link.png)

### Required Netbox User Permissions
The Plugin requires the following user permissions to access the topology view:

  - dcim | site   | Can read site
  - dcim | device | Can view device
  - dcim | cable  | Can view cable

  ## Contributing

Pull requests are welcomed and automatically built and tested against multiple version of Python and multiple version of Nautobot through TravisCI.

The project is packaged with a light development environment based on `docker-compose` to help with the local development of the project and to run the tests within TravisCI.

The project is following Network to Code software development guideline and is leveraging:

- Black, Pylint, Bandit and pydocstyle for Python linting and formatting.
- Django unit test to ensure the plugin is working properly.

### Development Environment

The development environment can be used in 2 ways. First, with a local poetry environment if you wish to develop outside of Docker. Second, inside of a docker container.

#### Invoke tasks

The [PyInvoke](http://www.pyinvoke.org/) library is used to provide some helper commands based on the environment.  There are a few configuration parameters which can be passed to PyInvoke to override the default configuration:

- `nautobot_ver`: the version of Nautobot to use as a base for any built docker containers (default: develop-latest)
- `project_name`: the default docker compose project name (default: aristacv-sync)
- `python_ver`: the version of Python to use as a base for any built docker containers (default: 3.6)
- `local`: a boolean flag indicating if invoke tasks should be run on the host or inside the docker containers (default: False, commands will be run in docker containers)
- `compose_dir`: the full path to a directory containing the project compose files
- `compose_files`: a list of compose files applied in order (see [Multiple Compose files](https://docs.docker.com/compose/extends/#multiple-compose-files) for more information)

Using PyInvoke these configuration options can be overridden using [several methods](http://docs.pyinvoke.org/en/stable/concepts/configuration.html).  Perhaps the simplest is simply setting an environment variable `INVOKE_ARISTACV-SYNC_VARIABLE_NAME` where `VARIABLE_NAME` is the variable you are trying to override.  The only exception is `compose_files`, because it is a list it must be overridden in a yaml file.  There is an example `invoke.yml` in this directory which can be used as a starting point.

#### Local Poetry Development Environment

1. Copy `development/creds.example.env` to `development/creds.env` (This file will be ignored by git and docker)
2. Uncomment the `POSTGRES_HOST`, `REDIS_HOST`, and `NAUTOBOT_ROOT` variables in `development/creds.env`
3. Create an invoke.yml with the following contents at the root of the repo:

```shell
---
aristacv_sync:
  local: true
  compose_files:
    - "docker-compose.requirements.yml"
```

4. Run the following commands:

```shell
poetry shell
poetry install
export $(cat development/dev.env | xargs)
export $(cat development/creds.env | xargs)
```

5. You can now run nautobot-server commands as you would from the [Nautobot documentation](https://nautobot.readthedocs.io/en/latest/) for example to start the development server:

```shell
nautobot-server runserver 0.0.0.0:8080 --insecure
```

Nautobot server can now be accessed at [http://localhost:8080](http://localhost:8080).

#### Docker Development Environment

**NOTE: Use WSL remote developement on Windows.**

This project is managed by [Python Poetry](https://python-poetry.org/) and has a few requirements to setup your development environment:

1. Install Poetry, see the [Poetry Documentation](https://python-poetry.org/docs/#installation) for your operating system.
2. Install Docker, see the [Docker documentation](https://docs.docker.com/get-docker/) for your operating system.

Once you have Poetry and Docker installed you can run the following commands to install all other development dependencies in an isolated python virtual environment:

```shell
poetry shell
poetry install
```
And then:
```shell
invoke start
```
Or this build debug target that instructs invoke to follow the container logs in the running terminal
```shell
invoke build debug
```

Nautobot server can now be accessed at [http://localhost:8080](http://localhost:8080).

### CLI Helper Commands

The project is coming with a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories `dev environment`, `utility` and `testing`.

Each command can be executed with `invoke <command>`. Environment variables `INVOKE_ARISTACV-SYNC_PYTHON_VER` and `INVOKE_ARISTACV-SYNC_NAUTOBOT_VER` may be specified to override the default versions. Each command also has its own help `invoke <command> --help`

#### Docker dev environment

```no-highlight
  build            Build all docker images.
  debug            Start Nautobot and its dependencies in debug mode.
  destroy          Destroy all containers and volumes.
  restart          Restart Nautobot and its dependencies.
  start            Start Nautobot and its dependencies in detached mode.
  stop             Stop Nautobot and its dependencies.
```

#### Utility

```no-highlight
  cli              Launch a bash shell inside the running Nautobot container.
  create-user      Create a new user in django (default: admin), will prompt for password.
  makemigrations   Run Make Migration in Django.
  nbshell          Launch a nbshell session.
```

#### Testing

```no-highlight
  bandit           Run bandit to validate basic static code security analysis.
  black            Run black to check that Python files adhere to its style standards.
  flake8           This will run flake8 for the specified name and Python version.
  pydocstyle       Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  pylint           Run pylint code analysis.
  tests            Run all tests for this plugin.
  unittest         Run Django unit tests for the plugin.
```

# Publishing Python Package
Remember to change the version in the corresponding files before publishing a new release and python package:
- ```pyproject.toml```
- ```setup.py```
- ```/nautobot_ui_plugin_docker/__init__.py```


## Questions

For any questions or comments, please check the [FAQ](FAQ.md) first and feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).
Sign up [here](http://slack.networktocode.com/)

