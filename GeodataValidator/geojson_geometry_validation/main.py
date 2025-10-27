import logging

from GeodataValidator.common.geojson_utils import GeoJsonUtils

LOGGER = logging.getLogger(__name__)

def validate_geojson_geometry(geojson_dict: dict)->bool:
    """
    Convert a geojson dict to a geojson object using geojson package and validate it.
    """
    LOGGER.info('Validating GeoJSON Geometry')
    gjutils = GeoJsonUtils()
    return gjutils.validate_geojson_geometry(geojson_dict)

if __name__ == "__main":
    geojson_dict = {"features":[{"geometry":{"coordinates":[[[9.4001,4.1678],[9.4001,4.1562],[9.4117,4.1562],[9.4117,4.1677],[9.4001,4.1678]]],"type":"Polygon"},"properties":{},"type":"Feature"}],"type":"FeatureCollection"}
    validate_geojson_geometry(geojson_dict)