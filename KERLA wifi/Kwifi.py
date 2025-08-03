import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from tqdm import tqdm

# Load your CSV file
df = pd.read_csv("Kwifi.csv", encoding="windows-1252")


# Initialize geocoder
geolocator = Nominatim(user_agent="kerala_wifi_mapper")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Add progress bar
tqdm.pandas()

# Get coordinates
df["Location"] = df["Location Address"].astype(str) + ", Kerala, India"
df["Coordinates"] = df["Location"].progress_apply(geocode)
df["Latitude"] = df["Coordinates"].apply(lambda loc: loc.latitude if loc else None)
df["Longitude"] = df["Coordinates"].apply(lambda loc: loc.longitude if loc else None)

# Drop rows without coordinates
df = df.dropna(subset=["Latitude", "Longitude"])

# Create the map
wifi_map = folium.Map(location=[10.8505, 76.2711], zoom_start=7)

# Add markers
for _, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["Location Name As Per List"],
        tooltip=row["Location Category"]
    ).add_to(wifi_map)

# Save the map
wifi_map.save("kerala_wifi_map.html")
