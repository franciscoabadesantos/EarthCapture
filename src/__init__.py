"""EarthCapture - Extract satellite images from Google Earth Pro and QGIS"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .geo_earth_pro.gep import ImageSet
from .geo_earth_pro import config

__all__ = ["ImageSet", "config"]
