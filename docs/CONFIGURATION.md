# Configuration

EarthCapture uses normalized UI coordinates stored in `src/geo_earth_pro/config.py`.

## Main Settings

- `UI_GEP`: mapping of UI element names to normalized coordinates
- `UI_GEP_SCREEN_SIZED`: coordinates scaled to the current screen size
- `IMAGES_FOLDER`: root directory for saved imagery
- `HISTORY_STEPS`: number of historical positions to capture
- `PAUSE_BETWEEN_ACTIONS`: delay between automation actions

## Recalibrating Coordinates

1. Open Google Earth Pro in the layout you intend to use.
2. Capture the positions of each relevant control.
3. Convert raw screen positions to normalized values by dividing:
   - x by screen width
   - y by screen height
4. Update the entries in `UI_GEP`.

## Batch Input CSV

The example CLI expects a CSV file with at least these columns:

```text
latitude,longitude
38.7301,-9.1890
38.7031,-9.4187
```
