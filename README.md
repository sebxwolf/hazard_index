# Goal: 

Given a hazard index indicating the probability of wildfires, come up with metrics that indicate potential economic losses in the endangered areas

# Strategy:

- import hazard index 
    - import and study the raw data
    - pick area of interest
- import data on the topography from openstreetmaps, study the individual parts
    - extract builing footprints
    - points of interest
    - network centrality
    - landuse
- convert into metrics correlated with economic losses 
    - size of building (area)
    - category of point of interest (value)
    - centrality of location (real estate price level)
    - landuse category (high-value (winery etc) or farmland)
- spatial merge the hazard index grid with the points and polygons with economic measures attached to them
- aggregate economic measures by pixel grid
- combine economic measures into an index
- analyse the result
