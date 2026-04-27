# API

## `src.geo_earth_pro.gep.ImageSet`

Primary automation class for Google Earth Pro capture.

### Constructor

```python
ImageSet(coordinates: str)
```

`coordinates` should be a string in the form `"latitude, longitude"`.

### Main Methods

- `start_downloading()`: search, zoom, capture current imagery, then walk backward through the configured history steps
- `display_coordinates()`: search and display the coordinates without running the full save flow
- `zoom_in()`: zoom to the configured target level

## `src.utils.calculation`

- `calculate_distance(lat1, lon1, lat2, lon2)`: Haversine distance in meters
- `divide_space(top_left, bottom_right, square_length, square_width)`: divide a rectangular extent into square tiles and return them in three row groups

## `src.qgis.google_map`

- `show_hybrid_google_map()`
- `show_satellite_google_map()`
- `show_road_google_map()`

These helpers are meant to run inside the QGIS Python environment.
