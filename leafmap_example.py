import leafmap
from ipywidgets import HTML

# Create a map centered on the US
m = leafmap.Map(center=[39.8283, -98.5795], zoom=4)

# Add a satellite basemap
m.add_basemap("SATELLITE")

# Add the GeoTIFF raster layer
m.add_raster("dem.tif", layer_name="DEM")

# Add a second raster layer to demonstrate multiple overlays
m.add_raster("dem.tif", layer_name="DEM (terrain)", colormap="terrain")

# Add the GeoJSON vector layer
m.add_geojson("states.geojson", layer_name="US States")

# Add a marker for Devil's Millhopper Park
m.add_marker(location=[29.70694, -82.39500], popup=HTML("Devil's Millhopper Park"))

# Add opacity control
m.add_opacity_control()

# Save the map to an HTML file
m.to_html("leafmap_example.html")

print("Map saved to leafmap_example.html")



# Add a marker for Devil's Millhopper Park
# m.add_marker(location=[29.70694, -82.39500], popup=HTML("Devil's Millhopper Park"))

# Add opacity control
m.add_opacity_control()

# Save the map to an HTML file
m.to_html("leafmap_example.html")

print("Map saved to leafmap_example.html")
