# 📶 Free WiFi Locations in Kerala

This project visualizes **Free WiFi locations across Kerala, India**, using publicly available government data. It allows users to explore these locations on an interactive map.

## 🔍 Data Source

The dataset used in this project was downloaded from the official Indian government open data portal:  
👉 [data.gov.in](https://www.data.gov.in/)

## 🗺️ Features

- Maps Free WiFi hotspots across various districts in Kerala.
- Geocodes location data using latitude and longitude.
- Interactive map display to visually explore coverage areas.

## ⚙️ Tech Stack

- **Python**
- `geopy` for geocoding addresses.
- `folium` for rendering interactive maps.
- `pandas` for data processing.

## 🐌 Note on Performance

This project uses the following from the `geopy` library:
- `geopy.geocoders.Nominatim`
- `geopy.extra.rate_limiter.RateLimiter`


⚠️ **Important Note**:  
Geocoding with `geopy` is **rate-limited to 1 request per second**, which means processing the full dataset can be **slow**. When testing or developing, it is **strongly recommended** to:
- Filter the data (e.g., by district or pincode).
- Use a subset of rows for faster results.
- use paid version 

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/kerala-free-wifi-map.git
   cd kerala-free-wifi-map

**This readme file is genrated using CPT ** 
