import leafmap

# Create a map centered on the US
m = leafmap.Map(center=[39.8283, -98.5795], zoom=4)

# Add a satellite basemap
m.add_basemap("SATELLITE")

# Add the GeoTIFF raster layer with 50% opacity
m.add_raster("dem.tif", layer_name="DEM (50% opacity)", opacity=0.5)

# Add a second raster layer to demonstrate multiple overlays with varying opacity
m.add_raster("dem.tif", layer_name="DEM (80% opacity)", opacity=0.8, colormap="terrain")

# Add the GeoJSON vector layer
m.add_geojson("states.geojson", layer_name="US States")

# Save the map to an HTML file
m.to_html("leafmap_example.html")

print("Map saved to leafmap_example.html")
