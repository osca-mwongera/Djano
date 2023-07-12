import django
import os

if __name__ == '__main__':
    django.setup()

    from django.contrib.gis.utils import LayerMapping

    from houses.models import District as houseDistrict
    from land.models import District as landDistrict

    district_mapping = {
        'distname': 'DISTNAME',
        'geom': 'MULTIPOLYGON',
    }

    shpFilePath = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'ke_district_boundaries/ke_district_boundaries.shp'))


    def load_data(verbose=True):
        hd_lm = LayerMapping(houseDistrict, shpFilePath, district_mapping, encoding='iso-8859-1', transform=False)
        hd_lm.save(verbose=verbose, strict=True)
        ld_lm = LayerMapping(landDistrict, shpFilePath, district_mapping, encoding='iso-8859-1', transform=False)
        ld_lm.save(verbose=verbose, strict=True)

    load_data()
