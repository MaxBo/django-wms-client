# coding=utf-8
"""Model Admin Class."""

from django import forms
from django.contrib import admin
from wms_client.models.wms_resource import (WMSResource,
                                            WMSLayer,
                                            LayerStyle,
                                            )


class WMSForm(forms.ModelForm):
    """Form for WMS entry including a password entry"""

    class Meta:
        model = WMSResource
        exclude = ('slug',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class WMSLayerInline(admin.StackedInline):
    model = WMSLayer


class LayerStyleInline(admin.StackedInline):
    model = LayerStyle


@admin.register(WMSResource)
class WMSResourceAdmin(admin.ModelAdmin):
    """Admin Class for WMSResource Model."""
    form = WMSForm
    list_display = ('name', 'uri')
    list_filter = ['name', 'uri']
    search_fields = ['name', 'description']
    inlines = [WMSLayerInline]


@admin.register(WMSLayer)
class WMSLayerAdmin(admin.ModelAdmin):
    """Admin for WMSLayer"""
    inlines = [LayerStyleInline]


@admin.register(LayerStyle)
class LayerStyleAdmin(admin.ModelAdmin):
    """Admin for LayerStyle"""
