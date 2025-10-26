import geojson
import shapely
import logging

LOGGER = logging.getLogger(__name__)

class GeoJsonUtils:

    def dumps_geojson_dict(self, geojson_dict: dict) -> str:
        geojson_dumps = geojson.dumps(geojson_dict)
        return geojson_dumps

    def geojson_obj_from_dumps(self, geojson_dumps: str) -> dict :
        geojson_obj = geojson.loads(geojson_dumps)
        return geojson_obj

    def feature_collection_from_geojson_obj(self, geojson_obj: dict) -> geojson.FeatureCollection:
        feature_collection = geojson.FeatureCollection(geojson_obj)
        return feature_collection

    def feature_collection_isvalid(self, feature_collection: geojson.FeatureCollection) -> bool:
        return feature_collection.is_valid

    def validate_geojson_geometry(self, geojson_dict: dict) -> bool:
        is_valid = True
        for feature in geojson_dict['features']:
            geom = shape(feature['geometry'])
            is_valid = bool(shapely.is_valid(geom))
            if is_valid == False:
                LOGGER.warning(shapely.validation.explain_validity(geom))
                break
        return is_valid
