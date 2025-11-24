import logging
import geojson_validator
import shapely
from shapely.geometry import shape
from shapely.validation import explain_validity

LOGGER = logging.getLogger(__name__)
#geojson_validator.configure_logging(enabled=False)

class GeoJsonUtils:

    def geojson_isvalid(self, geojson: dict) -> bool:
        validity_report = geojson_validator.validate_structure(geojson)
        return validity_report

    def validate_geojson_geometry(self, geojson: dict) -> bool:
        validity_report = geojson_validator.validate_geometries(geojson)
        return validity_report