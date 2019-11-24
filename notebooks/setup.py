##### Import packages #####

### data wrangling
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option("display.max_rows", 100)
pd.options.display.max_columns = 100
import datetime as dt
import numpy as np
from random import sample, seed
seed(510)
import re
import geopandas as gpd
import copy
import json
from shapely.geometry import Polygon, MultiPolygon
import osmnx as ox
from networkx import betweenness_centrality

### plotting
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import chart_studio.plotly as py
import plotly.graph_objs as go
import seaborn as sns
import folium
from folium.plugins import HeatMap, DualMap, Fullscreen
from folium.features import DivIcon
from branca.element import Template, MacroElement
import locale
from mpl_toolkits.axes_grid1 import make_axes_locatable

### jupyter
from IPython.display import HTML
import warnings
warnings.filterwarnings('ignore')
import os
from IPython.display import display, HTML

display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))
