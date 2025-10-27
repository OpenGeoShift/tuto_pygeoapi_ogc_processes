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