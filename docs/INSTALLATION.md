# Installation

## Requirements

- Python 3.8+
- Google Earth Pro
- A desktop session where `pyautogui` can move the mouse and interact with windows

QGIS is optional and only needed for the helpers in `src/qgis/google_map.py`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Sanity Check

1. Open Google Earth Pro manually.
2. Verify that your display scaling and window layout match the coordinates in `src/geo_earth_pro/config.py`.
3. Run:

```bash
python examples/extract_images.py --csv data/sample_coordinates.csv --limit 1
```
