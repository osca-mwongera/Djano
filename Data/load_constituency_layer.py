import os

from django.contrib.gis.utils import LayerMapping

from houses.models import Constituency

constituency_mapping = {
    'objectid': 'OBJECTID',
    'const_nam': 'CONST_NAM',
    'const_no': 'CONST_NO',
    'county_nam': 'COUNTY_NAM',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

shpFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Constituency.shp'))


def load_data(verbose=True):
    lm = LayerMapping(Constituency, shpFilePath, constituency_mapping, encoding='iso-8859-1', transform=False)
    lm.save(verbose=verbose, strict=True)
