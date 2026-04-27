# EarthCapture

Automated extraction of satellite imagery from Google Earth Pro and QGIS. Download high-resolution satellite images for specific geographic coordinates with historical image support.

## Features

- **Automated Google Earth Pro Control** - Use pyautogui to automate image capture from Google Earth Pro
- **Historical Imagery** - Download satellite images from multiple dates for time-series analysis
- **Batch Processing** - Extract images for multiple coordinates programmatically
- **Automatic Organization** - Images organized by date (YYYY/MM/DD folder structure)
- **QGIS Integration** - Alternative method using QGIS for image capture and georeferencing
- **Configurable Zoom Levels** - Adjust zoom and resolution for different use cases
- **Internet Connectivity Monitoring** - Automatic retry on connection loss

## Installation

### Prerequisites

- **Google Earth Pro** (free or Pro version) - [Download here](https://www.google.com/earth/download/)
- **Python 3.8+**
- **Windows OS** (tested on Windows 10/11, can be adapted for macOS/Linux)

### Optional

- **QGIS** (for alternative extraction method) - [Download here](https://qgis.org/download/)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/EarthCapture.git
cd EarthCapture
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Google Earth Pro coordinates (see Configuration section below)

## Quick Start

### Method 1: Google Earth Pro Automation

```python
from src.geo_earth_pro.gep import ImageSet

# Extract images for a single location
coords = "38.7301, -9.1890"  # Format: latitude, longitude
image_set = ImageSet(coords)
image_set.start_downloading()
```

### Method 2: Batch Processing

```python
import pandas as pd
from src.geo_earth_pro.gep import ImageSet

# Load coordinates from CSV
df = pd.read_csv('coordinates.csv')

for idx, row in df.iterrows():
    coords = f"{row['latitude']}, {row['longitude']}"
    print(f"Extracting {idx+1}/{len(df)}: {coords}")
    
    image_set = ImageSet(coords)
    image_set.start_downloading()
```

### Method 3: Using QGIS

```python
from src.qgis.google_map import show_satellite_google_map

# In QGIS Python console
layer = show_satellite_google_map()
```

## Configuration

### Google Earth Pro UI Coordinates

Edit `src/geo_earth_pro/config.py` to match your screen resolution:

```python
UI_GEP = {
    'searchField': (11/1920, 94/1080),      # Search box location
    'searchButton': (354/1920, 93/1080),    # Search button location
    'zoomIn': (1875/1920, 291/1080),        # Zoom in button
    # ... more coordinates
}

# Output folder
IMAGES_FOLDER = './output'

# Number of historical images to download
HISTORY_STEPS = 3
```

**To find UI coordinates:**
1. Run the coordinate finder:
```bash
python -m pyautogui position
```
2. Move mouse to each UI element and note the coordinates
3. Update the config file (divide by 1920 and 1080 for normalization)

### Output Structure

```
output/
├── 2024/
│   ├── 01/
│   │   ├── 15/
│   │   │   ├── image_1.jpg
│   │   │   └── image_2.jpg
│   ├── 02/
│   └── ...
├── 2023/
├── 2022/
└── ...
```

## Architecture

### Core Modules

- **`src/geo_earth_pro/gep.py`** - Main ImageSet class for Google Earth Pro automation
- **`src/geo_earth_pro/config.py`** - UI coordinates and configuration
- **`src/utils/calculation.py`** - Geospatial calculations (distance, grid generation)
- **`src/qgis/google_map.py`** - QGIS layer loading functions

### Key Classes

#### ImageSet
```python
class ImageSet:
    """Automates satellite image download from Google Earth Pro"""
    
    def start_downloading(self)
        """Download current and historical imagery"""
    
    def display_coordinates(self)
        """Display coordinates without downloading"""
    
    def zoom_in(self)
        """Zoom to target level"""
```

## Usage Examples

### Single Image Download
```python
from src.geo_earth_pro.gep import ImageSet

image_set = ImageSet("38.7301, -9.1890")
image_set.start_downloading()
```

### Processing Large Areas
```python
from src.utils.calculation import divide_space

# Divide geographic area into grid
squares1, squares2, squares3 = divide_space(
    top_left=(38.8, -9.3),
    bottom_right=(38.6, -9.0),
    square_length=1000,  # meters
    square_width=1000
)

# Extract images for each square center
for squares in [squares1, squares2, squares3]:
    for top_left, bottom_right, center in squares:
        coords = f"{center[0]}, {center[1]}"
        print(f"Extracting: {coords}")
        image_set = ImageSet(coords)
        image_set.start_downloading()
```

### Time-Series Analysis
```python
image_set = ImageSet("38.7301, -9.1890")
image_set.start_downloading()  # Gets current + historical images
```

## Troubleshooting

### Issue: UI Elements Not Clicked Correctly

**Solution:** Update coordinates in `config.py`
```bash
python -m pyautogui position
```

### Issue: Images Not Saving

**Solution:** Check output folder path:
- Ensure folder exists
- Check write permissions
- Verify disk space available

### Issue: Connection Timeouts

**Solution:** Check internet connectivity
```bash
ping www.google.com
```

### Issue: Google Earth Pro Not Responding

**Solution:** 
- Restart Google Earth Pro
- Increase `PAUSE_BETWEEN_ACTIONS` in config.py
- Check system resources

## Coordinate Format

Coordinates should be in **decimal degrees format** (WGS84):

```
latitude, longitude

Examples:
38.7301, -9.1890      # Caparica, Portugal
51.5074, -0.1278      # London, UK
40.7128, -74.0060     # New York, USA
```

## Output Formats

Downloaded images include:
- **JPEG files** - Satellite imagery
- **PGW world files** - Georeferencing information
- **XML metadata** - Image properties

## Limitations

- **Windows Only** - Currently requires Windows OS (pyautogui has limited support for other OSs)
- **Single Monitor** - Works with single primary monitor
- **Manual Calibration** - UI coordinates need adjustment for different screen resolutions
- **Google Earth Pro Required** - Needs Google Earth Pro to be installed and running
- **Rate Limiting** - Respect Google Earth Pro terms of service

## Performance Tips

1. **Batch Processing**: Process multiple locations sequentially to avoid window conflicts
2. **Schedule Downloads**: Run during off-peak hours
3. **Cache Results**: Store downloaded coordinates to avoid re-downloading
4. **Optimize Zoom**: Adjust zoom level based on your region of interest

## Project Structure

```
SatelliteImagery-Extractor/
├── src/
│   ├── geo_earth_pro/
│   │   ├── gep.py           # Main ImageSet class
│   │   └── config.py        # UI coordinates
│   ├── qgis/
│   │   └── google_map.py    # QGIS functions
│   └── utils/
│       └── calculation.py   # Geospatial utilities
├── examples/
│   └── extract_images.py    # Usage examples
├── docs/
│   ├── INSTALLATION.md      # Installation guide
│   ├── CONFIGURATION.md     # Configuration guide
│   └── API.md              # API reference
├── data/
│   └── sample_coordinates.csv
├── images/                  # Sample images
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Cross-platform support (macOS, Linux)
- [ ] Multi-monitor support
- [ ] Web UI for coordinate input
- [ ] Batch coordinate file support (GeoJSON, Shapefile)
- [ ] Image quality analysis
- [ ] Automatic coordinate calibration
- [ ] Google Earth Engine integration
- [ ] Bing Maps support

## Related Projects

- **PixelVision** - Computer vision-based object detection on satellite images
- [Google Earth Pro](https://www.google.com/earth/download/)
- [QGIS](https://qgis.org/)
- [pyautogui](https://pyautogui.readthedocs.io/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational and research purposes only. Please ensure you have appropriate permissions before downloading satellite imagery for commercial use. Respect Google's terms of service when using Google Earth Pro.

## Citation

If you use this tool in your research, please cite:

```bibtex
@software{earthcapture,
  title={EarthCapture - Satellite Imagery Extractor},
  author={Your Name},
  year={2024},
  url={https://github.com/yourusername/EarthCapture}
}
```

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/SatelliteImagery-Extractor/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/SatelliteImagery-Extractor/discussions)
- **Email**: your.email@example.com

---

**Last Updated**: 2024  
**Version**: 1.0.0
