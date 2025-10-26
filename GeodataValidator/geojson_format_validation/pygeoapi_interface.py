import logging
import traceback

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError
from . import validate_geojson_format

LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.2.0',
    'id': 'geojson-format-validation',
    'title': {
        'en': 'Geojson Format Validation',
        'fr': 'Validation Format Geojson'
    },
    'description': {
        'en': 'Validate Geojson Format',
        'fr': 'Valide Geojson Format',
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['geojson', 'format', 'validation'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'geojson': {
            'title': 'Geojson',
            'description': 'Geojson',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'keywords': ['geojson']
        }
    },
    'outputs': {
        'is_format_valid': {
            'title': 'Is geojson format valid',
            'description': 'Is the geojson format provided valid',
            'schema': {
                'type': 'boolean'
            }
        }
    },
    'example': {
        'inputs': {
            'geojson': {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"coordinates":[[[9.4001,4.1678],[9.4001,4.1562],[9.4117,4.1562],[9.4117,4.1677],[9.4001,4.1678]]],"type":"Polygon"}}]},
        }
    }
}


class GeoJsonFormatValidatorProcessor(BaseProcessor):
    """Hello World Processor example"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.geojson_format_validation.GeoJsonFormatValidatorProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)
        self.supports_outputs = True

    def execute(self, data, outputs=None):
        mimetype = 'application/json'
        geojson = data.get('geojson')

        if geojson is None:
            raise ProcessorExecuteError('Cannot process without a geojson')

        try:
            is_format_valid = validate_geojson_format.validate_geojson_format(geojson)
            outputs = {"is_format_valid": is_format_valid}

        except Exception as err:

            err_name = {type(err).__name__}
            err_message = repr(err)
            traceback_info = repr(traceback.format_exc())

            LOGGER.error(f"{err_name} - {err_message} - {traceback_info}")
            raise ProcessorExecuteError(f'{err_name} - {err_message}')

        return mimetype, outputs

    def __repr__(self):
        return f'<GeoJsonFormatValidatorProcessor> {self.name}'
