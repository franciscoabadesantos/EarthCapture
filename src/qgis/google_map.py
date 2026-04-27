"""
QGIS integration for displaying and capturing satellite imagery.
"""

import requests
from qgis.utils import iface


def show_hybrid_google_map():
    """
    Add Google Hybrid map layer to QGIS.
    
    Returns:
        QgsRasterLayer: The added raster layer
    """
    service_url = "mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}"
    service_uri = f"type=xyz&zmin=0&zmax=21&url=https://{requests.utils.quote(service_url)}"
    tms_layer = iface.addRasterLayer(service_uri, "Google Hybrid", "wms")
    return tms_layer


def show_satellite_google_map():
    """
    Add Google Satellite map layer to QGIS.
    
    Returns:
        QgsRasterLayer: The added raster layer
    """
    service_url = "mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
    service_uri = f"type=xyz&zmin=0&zmax=21&url=https://{requests.utils.quote(service_url)}"
    tms_layer = iface.addRasterLayer(service_uri, "Google Satellite", "wms")
    return tms_layer


def show_road_google_map():
    """
    Add Google Road map layer to QGIS.
    
    Returns:
        QgsRasterLayer: The added raster layer
    """
    service_url = "mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
    service_uri = f"type=xyz&zmin=0&zmax=21&url=https://{requests.utils.quote(service_url)}"
    tms_layer = iface.addRasterLayer(service_uri, "Google Road", "wms")
    return tms_layer


def on_render_complete():
    """Called when rendering is complete."""
    print("Rendering complete")
