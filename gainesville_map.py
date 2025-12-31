import leafmap
from ipywidgets import HTML

# Create a map centered on Gainesville, Florida
m = leafmap.Map(center=(29.6516, -82.3248), zoom=12)

# Define the image URL and its geographic boundaries
image_url = "Screenshot_20251230-123717.png"
bounds = [[29.6393, -82.3950], [29.7069, -82.32035]]

# Add the image overlay to the map
m.image_overlay(image_url, bounds, name="Gainesville Overlay")

# Add a marker for the reference point
m.add_marker(location=(29.7069, -82.3950), popup=HTML("Reference Point"))

# Save the map to an HTML file
m.to_html("gainesville_map.html")

print("Map created and saved to gainesville_map.html")
