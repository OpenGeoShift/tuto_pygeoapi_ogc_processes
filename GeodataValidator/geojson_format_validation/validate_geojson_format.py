import logging
from GeodataValidator.common.geojson_utils import GeoJsonUtils

LOGGER = logging.getLogger(__name__)

def validate_geojson_format(geojson_dict: dict)->bool:
    """
    Convert a geojson dict to a geojson object using geojson package and validate it.
    """
    LOGGER('Validating GeoJSON Format')
    gjutils = GeoJsonUtils()
    geojson_dumps = gjutils.dumps_geojson_dict(geojson_dict)
    geojson_obj  = gjutils.geojson_obj_from_dumps(geojson_dumps)
    feature_collection = gjutils.feature_collection_from_geojson_obj(geojson_obj)
    return gjutils.feature_collection_isvalid(feature_collection)