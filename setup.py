from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='nautobot_ui_plugin_docker',
    version='0.0.2',
    url='https://gitlab-ce.gwdg.de/gwdg-netz/nautobot-plugins/nautobot-ui-plugin/',
    # download_url='https://github.com/iDebugAll/nextbox-ui-plugin/archive/v0.9.2.tar.gz',
    description='A topology visualization plugin for Nautobot powered by NextUI Toolkit.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen',
    author_email='netzadmin@gwdg.de',
    install_requires=[],
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    keywords=['nautobot', 'nautobot-plugin', 'plugin'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
