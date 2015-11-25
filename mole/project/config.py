import os

from platform import system
from qgis.core import QgsRectangle

import mole


# County
country = 'Germany'

# Project information
project_crs = 'EPSG:3857'
measurement_projection='EPSG:32633'
### Information needed to use external plugins
# OpenStreetMap plugin
ol_plugin_name = 'openlayers_plugin'
open_layer_type_id = 4
# id=0 - Google Physical
# id=1 - Google Streets
# id=4 - OpenStreetMap
open_layers_layer_name='OpenStreetMap'
# Point Sampling Tool
pst_plugin_name = 'pointsamplingtool'
pst_output_layer_name = 'PS Results'
pst_input_layer_name = 'BLD Centroids'

# Realcentroid plugin
real_centroid_plugin_name = 'realcentroid'

### Default values
# default extent is set, after the OSM-layer was loaded (currently: extent of Germany)
x = 10.447683
y = 51.163375
scale = 0.5
default_extent = QgsRectangle(x - scale, y - scale, x + scale, y + scale)
default_extent_crs = 'EPSG:3857'

# name of the shapefile which will be created to define the investigation area
investigation_shape_layer_name = 'Investigation Area'
investigation_shape_layer_style = 'oeq_ia_style.qml'

housing_layer_name = 'BLD Shapes'
building_outline_style ='oeq_floor_sw.qml'
housing_coordinate_layer_name = 'BLD Centroids'
data_layer_name = 'BLD Data'


# name of the wms-raster which will be loaded and is the basis for the clipping
clipping_raster_layer_name = 'Investigation Area - raster'
color_match_tolerance = 80


### Default paths
plugin_dir = os.path.dirname(mole.__file__)
progress_model = os.path.join(plugin_dir, 'project', 'default_progress.oeq')
investigation_area_style = os.path.join(plugin_dir, 'styles', 'oeq_ia_style.qml')
valid_centroids_style = os.path.join(plugin_dir, 'styles', 'oeq_valid_centroid_style.qml')

def qgis_prefix_path():
    if system() == 'Windows':
        return 'D:/OSGEO4~1/apps/qgis'
    else:
        return '/Applications/QGIS.app/Contents/MacOS'


default_heating_degree_days =  2750
default_average_build_year =  1950
default_population_density =  10000

# default_projectinfo
pinfo_default = {
    'project_name': u'New Project',
    'description': u'',
    'location_city': u'',
    'location_postal': u'',
    'location_lon': u'',
    'location_lat': u'',
    'location_crs': u'',
    'heating_degree_days': default_heating_degree_days,
    'average_build_year': default_average_build_year,
    'population_density': default_population_density
}
