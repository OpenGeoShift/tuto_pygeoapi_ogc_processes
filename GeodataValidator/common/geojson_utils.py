import logging
import geojson_validator
#from pydantic_geojson import FeatureCollectionModel
#from pydantic import ValidationError

LOGGER = logging.getLogger(__name__)
#geojson_validator.configure_logging(enabled=False)

class GeoJsonUtils:
    """
    def geojson_isvalid(self, geojson: dict) -> bool:
        try:
            feature_collection = FeatureCollectionModel(**data)
            return True
        except ValidationError as e:
            LOGGER.error(e)
            return False

    def validate_geojson_geometry(self, geojson: dict) -> bool:
        return True

    """

    def geojson_isvalid(self, geojson: dict) -> bool:
        validity_report = geojson_validator.validate_structure(geojson)
        return validity_report

    def validate_geojson_geometry(self, geojson: dict) -> bool:
        validity_report = geojson_validator.validate_geometries(geojson)
        return validity_report
