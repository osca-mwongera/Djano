import os

from django.contrib.gis.utils import LayerMapping

from houses.models import District


district_mapping = {
    'distname': 'DISTNAME',
    'geom': 'MULTIPOLYGON',
}

shpFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'ke_district_boundaries/ke_district_boundaries.shp'))


def load_data(verbose=True):
    lm = LayerMapping(District, shpFilePath, district_mapping, encoding='iso-8859-1', transform=False)
    lm.save(verbose=verbose, strict=True)
