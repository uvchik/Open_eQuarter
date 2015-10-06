# -*- coding: utf-8 -*-

from qgis.core import NULL
from mole.project import config

def calculation(self=None, parameters={}):
    from PyQt4.QtCore import QVariant
    from qgis.core import NULL
    result = {self.field_id + '_P': {'type': QVariant.String,
                                     'value': self.layer_name},
              'FLOORS': {'type': QVariant.Double,
                         'value': NULL}}
    if parameters != {}:
        try:
            result['FLOORS']['value'] = sum([float(i) for i in parameters.values()]) / len(parameters)
        except:
            result['FLOORS']['value'] = 3.5
    else:
           result['FLOORS']['value'] = 3.5
    return result


import os
from mole.extensions import OeQExtension

extension = OeQExtension(
    extension_id=__name__,
    category='Import',
    subcategory='WMS',
    extension_name='Floors (ALK Berlin, WMS)',
    field_id='FLRS',
    source_type='wms',
    layer_name='Floors (WMS Capture)',
    active=True,
    description=u'',
    source='crs=EPSG:4326&dpiMode=7&format=image/png&layers=2&styles=&url=http://fbinter.stadt-berlin.de/fb/wms/senstadt/alk_gebaeude',
    extension_filepath=os.path.join(__file__),
    colortable = os.path.join(os.path.splitext(__file__)[0] + '.qml'),
    evaluation_method=calculation)

extension.registerExtension(default=True)