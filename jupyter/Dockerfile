FROM jupyter/datascience-notebook

RUN python --version

RUN conda install --quiet --yes -c \
    conda-forge osmnx dask jupyter_contrib_nbextensions jupyter_nbextensions_configurator

RUN pip install -U geopandas \
                   geopy \
                   rtree \
                   folium \
                   shapely \
                   fiona \
                   six \
                   pyproj \
                   numexpr==2.6.4 \
                   elasticsearch \
                   geojson \
                   plotly \
                   tqdm \
                   mapboxgl \
                   cufflinks \
                   geohash2 \
                   tables \
                   mixpanel \
                   GeoAlchemy2

VOLUME /notebooks
WORKDIR /notebooks
