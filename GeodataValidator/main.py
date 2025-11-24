import logging
import time

from GeodataValidator.common.geojson_utils import GeoJsonUtils

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

gjutils = GeoJsonUtils()

def validate_geojson_format(geojson: dict)->bool:
    """
    Validate geojson structure
    """
    LOGGER.info('Validating GeoJSON Format')
    #time.sleep(10)
    return gjutils.geojson_isvalid(geojson)

def validate_geojson_geometry(geojson: dict)->bool:
    """
    Validate geojson geometry
    """
    LOGGER.info('Validating GeoJSON Geometry')
    #time.sleep(10)
    return gjutils.validate_geojson_geometry(geojson)

if __name__ == "__main__":

    geojson = {"features":[{"geometry":{"coordinates":[[[9.4001,4.1678],[9.4001,4.1562],[9.4117,4.1562],[9.4117,4.1677],[9.4001,4.1678]]],"type":"Polygon"},"properties":{},"type":"Feature"}],"type":"FeatureCollection"}

    geojson_validation_result = validate_geojson_format(geojson)
    if geojson_validation_result:
        raise Exception(geojson_validation_result)
    LOGGER.info(f'format validated')

    geometry_validation_result = validate_geojson_geometry(geojson)
    if geometry_validation_result['invalid'] or geometry_validation_result['problematic']:
        raise Exception(geometry_validation_result)
    LOGGER.info(f'geometry validated')