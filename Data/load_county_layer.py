import django
import os

if __name__ == '__main__':
    django.setup()

    from django.contrib.gis.utils import LayerMapping

    from land.models import County as landCounty
    from houses.models import County as houseCounty

    county_mapping = {
        'objectid': 'OBJECTID',
        'unit_area': 'UNIT_AREA',
        'unit_perim': 'UNIT_PERIM',
        'district': 'DISTRICT',
        'count_field': 'COUNT_',
        'county_nam': 'COUNTY_NAM',
        'code': 'CODE',
        'shape_leng': 'Shape_Leng',
        'shape_area': 'Shape_Area',
        'geom': 'MULTIPOLYGON',
    }

    shpFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'County.shp'))


    def load_data(verbose=True):
        lc_lm = LayerMapping(landCounty, shpFilePath, county_mapping, encoding='iso-8859-1', transform=False)
        lc_lm.save(verbose=verbose, strict=True)
        hc_lm = LayerMapping(houseCounty, shpFilePath, county_mapping, encoding='iso-8859-1', transform=False)
        hc_lm.save(verbose=verbose, strict=True)

    load_data()
