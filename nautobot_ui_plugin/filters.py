import django_filters
from nautobot.dcim.models import Device, Site, Region, RackGroup, DeviceRole
from nautobot.tenancy.models import Tenant, TenantGroup
from nautobot.extras.models import Tag
from django.conf import settings
from packaging import version
from nautobot.utilities.filters import TreeNodeMultipleChoiceFilter



class TopologyFilterSet(django_filters.FilterSet):

    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        to_field_name='id',
        field_name='id',
        label='Device (ID)',
    )
    device_role_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DeviceRole.objects.all(),
        label='Device Role (ID)',
    )
    rack_group_id = TreeNodeMultipleChoiceFilter(
        queryset=RackGroup.objects.all(),
        label='RackGroup (ID)',
        field_name='rack__group',
        lookup_expr="in",
    )
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        label='Site (ID)',
    )
    region_id = TreeNodeMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='site__region',
        label='Region (ID)',
        lookup_expr="in",
    )
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant (ID)',
        field_name='tenant'
    )
    tenant_group_id = TreeNodeMultipleChoiceFilter(
        queryset=TenantGroup.objects.all(),
        label='TenantGroup (ID)',
        field_name='tenant__group',
        lookup_expr="in",
    )
    tag_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        label='Tag (ID)',
        field_name='tags'
    )
    class Meta:
        model = Device
        fields = ['id', 'name', ]
