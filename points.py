import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import Point

# Set a random seed so that the output will be reproducible
np.random.seed(12)


# Load boundaries for the 9-county San Francisco Bay Area

# Derived from the 2016 TIGER/Line shapefile of US counties:
# ftp://ftp2.census.gov/geo/tiger/TIGER2016//COUNTY/tl_2016_us_county.zip

bayarea = gpd.read_file('input/tl_2016_us_county_bayarea/tl_2016_us_county_bayarea.shp')
print bayarea.head()


# Project into meters

print bayarea.crs

# EPSG 4269 is NAD83 without a projection - https://epsg.io/4269
# We'll project into California Albers in meters - https://epsg.io/3488 

bayarea = bayarea.to_crs(epsg=3488)
print bayarea.crs


# Generate random points

bayarea_geom = bayarea.unary_union  # Shapely MultiPolygon
print bayarea_geom.bounds  # bounding box: (min, max, min, max)

(a, b, c, d) = bayarea_geom.bounds


def rand(min, max):
    """ 
    Generate a random float uniformly distributed from `min` to `max`.
    
    """
    return (max - min) * np.random.rand() + min


def reproject(geom, in_epsg, out_epsg):
    """ 
    Shapely doesn't support projections or coordinate reference systems. This function 
    re-projects a Shapely geometry object via GeoPandas. 
    
    """
    df = pd.DataFrame([geom], columns=['geometry'])
    gdf = gpd.GeoDataFrame(df)
    gdf.crs = {'init': 'epsg:' + str(in_epsg)}
    gdf = gdf.to_crs(epsg = out_epsg)
    return gdf.geometry[0]
    

id = 1
output = []

while id <= 10:
    
    # Generate a random point inside the bounding box
    p = Point(rand(a, b), rand(c, d))
    
    # Check if it's within the MultiPolygon
    if p.within(bayarea_geom):
        
        # Convert the coordinates from meters to lon-lat
        p = reproject(p, 3488, 4326)  # WGS84 unprojected - https://epsg.io/4326 
        output.append([id, p.x, p.y])
        id += 1


print output

# Save id, lat/lon, link to Google


# Save as CSV and as GeoJSON

