# Geospatial Data Overlay with Leafmap

This project provides a Python script that demonstrates how to use the `leafmap` library to create an interactive map with multiple data overlays.

## Overview

The `leafmap_example.py` script generates an HTML map that includes:

*   A satellite basemap.
*   A GeoTIFF raster layer with 50% opacity.
*   A second GeoTIFF raster layer with 80% opacity and a "terrain" colormap.
*   A GeoJSON vector layer representing the US states.

The final map is saved to `leafmap_example.html`.

## How to Run

1.  **Install dependencies:**

    ```bash
    pip install leafmap
    ```

2.  **Download the sample data:**

    *   GeoTIFF: [https://www.intermap.com/hubfs/NEXTMap%206%20Samples/NM6%20v1_n48e003g7dsm.tif](https://www.intermap.com/hubfs/NEXTMap%206%20Samples/NM6%20v1_n48e003g7dsm.tif) (save as `dem.tif`)
    *   GeoJSON: [https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json](https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json) (save as `states.geojson`)

3.  **Run the script:**

    ```bash
    python leafmap_example.py
    ```

4.  **View the output:**

    Open the generated `leafmap_example.html` file in your web browser.
