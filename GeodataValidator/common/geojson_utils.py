import logging
from pydantic_geojson import FeatureCollectionModel
from pydantic import ValidationError
from shapely.geometry import shape
from shapely.validation import explain_validity

LOGGER = logging.getLogger(__name__)

class GeoJsonUtils:

    def geojson_isvalid(self, geojson: dict) -> bool:

        try:
            FeatureCollectionModel(**geojson)
            return True
        except ValidationError as e:
            LOGGER.error(e)
            return False

    def validate_geojson_geometry(self, geojson: dict) -> bool:

        all_valid = True

        for idx, feature in enumerate(geojson.get("features", [])):

            geom = feature.get("geometry")

            if geom is None:
                LOGGER.warning(f"Feature {idx}: missing geometry")
                all_valid = False
                continue

            shapely_geom = shape(geom)

            if not shapely_geom.is_valid:
                LOGGER.error(f"Feature {idx}: invalid geometry")
                LOGGER.error(f"  Reason: {explain_validity(shapely_geom)}")
                all_valid = False

        return all_valid