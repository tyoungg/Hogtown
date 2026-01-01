import leafmap
from ipywidgets import HTML

# Create a map centered on Gainesville, Florida
m = leafmap.Map(center=(29.6516, -82.3248), zoom=12)

# Add the GeoTIFF raster layer
m.add_raster("gainesville_overlay.tif", layer_name="Gainesville Overlay")

# Add a marker for Devil's Millhopper Park
m.add_marker(location=(29.7069, -82.3950), popup=HTML("Devil's Millhopper Park"))

# Add opacity control
m.add_opacity_control()

# Save the map to an HTML file
m.to_html("gainesville_map.html")

print("Map created and saved to gainesville_map.html")
