from django import forms
from nautobot.ipam.models import VLAN
from nautobot.utilities.forms import (
    BootstrapMixin,
    DynamicModelMultipleChoiceField,
    DynamicModelChoiceField
)
from .models import NautobotSavedTopology
from nautobot.dcim.models import Device, Site, Region, RackGroup, DeviceRole
from nautobot.tenancy.models import Tenant, TenantGroup
from nautobot.extras.models import Tag
from django.conf import settings
from packaging import version


class TopologyFilterForm(BootstrapMixin, forms.Form):

    model = Device

    device_id = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
        label='Device'
    )
    device_role_id = DynamicModelMultipleChoiceField(
        queryset=DeviceRole.objects.all(),
        to_field_name='id',
        required=False,
        null_option='None',
        label='Device Role'
    )
    rack_group_id = DynamicModelMultipleChoiceField(
        queryset=RackGroup.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
        label='Rack Group'
    )
    site_id = DynamicModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
        label='Site'
    )
    vlan_id = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
        label='VLAN'
    )
    region_id = DynamicModelMultipleChoiceField(
        queryset=Region.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
        label='Region'
    )
    tenant_id = DynamicModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
        label='Tenant'
    )
    tenant_group_id = DynamicModelMultipleChoiceField(
        queryset=TenantGroup.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
        label='Tenant Group'
    )
    tag_id = DynamicModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        to_field_name='id',
        null_option='None',
        label='Tag'
    )


class LoadNautobotSavedTopologyFilterForm(BootstrapMixin, forms.Form):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(LoadNautobotSavedTopologyFilterForm, self).__init__(*args, **kwargs)
        self.fields['saved_topology_id'].queryset = NautobotSavedTopology.objects.filter(created_by=user)

    model = NautobotSavedTopology

    saved_topology_id = forms.ModelChoiceField(
        queryset=None,
        to_field_name='id',
        required=True
    )
