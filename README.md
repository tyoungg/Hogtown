# Leafmap Examples

This project provides a collection of Python scripts demonstrating the use of the `leafmap` library to create interactive maps with various data overlays.

## Dependencies

The following Python libraries are required to run the examples:

- `leafmap`
- `ipywidgets`
- `xarray`
- `rasterio`
- `localtileserver`

You can install them using pip:

```bash
pip install leafmap ipywidgets xarray rasterio localtileserver
```

## Usage

Each Python script can be run directly from the command line. They will generate HTML files containing the interactive maps.

```bash
python gainesville_map.py
python leafmap_example.py
```

## Examples

### `gainesville_map.py`

This script creates an interactive map centered on Gainesville, Florida.

-   **Basemap:** Uses a satellite basemap.
-   **Image Overlay:** Overlays a PNG image (`Screenshot_20251230-123717.png`) of a topographical map onto the basemap with a specified opacity.
-   **Marker:** Adds a marker for Sweetwater Wetlands Park with a popup message.
-   **Output:** Generates an `gainesville_map.html` file.

### `leafmap_example.py`

This script demonstrates how to add raster and vector data to a map.

-   **Basemap:** Uses a satellite basemap.
-   **Raster Layer:** Adds a GeoTIFF raster file (`dem.tif`) representing a digital elevation model.
-   **Vector Layer:** Adds a GeoJSON file (`states.geojson`) containing US state boundaries.
-   **Layer Control:** Adds a layer control to toggle the visibility of the raster and vector layers.
-   **Output:** Generates a `map.html` file.
