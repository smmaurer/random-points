import pandas as pd
import geopandas as gpd

# Load boundaries for the bay area

# Derived from the 2016 TIGER/Line shapefile of US counties, this includes the 9 counties
# that make up ABAG --
# ftp://ftp2.census.gov/geo/tiger/TIGER2016//COUNTY/tl_2016_us_county.zip

bayarea = gpd.read_file('input/tl_2016_us_county_bayarea/tl_2016_us_county_bayarea.shp')
print bayarea.head()

# Project into meters

print bayarea.crs

# EPSG 4269 is NAD83 without a projection - https://epsg.io/4269
# We'll project into California Albers in meters - https://epsg.io/3488 

bayarea = bayarea.to_crs(epsg=3488)
print bayarea.crs

# Generate random points within min/max bounds





# Check if they're within the shapefile bounds


# Save id, lat/lon, link to Google


# Save as CSV and as GeoJSON


# Stop when we have 100