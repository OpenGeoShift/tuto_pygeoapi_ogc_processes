from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError
from GeodataValidator import main

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.2.0',
    'title': {
        'en': 'geojson-format-validation',
        'fr': 'geojson-format-validation'
    },
    'description': {
        'en': 'Validate geojson format',
        'fr': 'Validation format geojson',
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
        'is_valid': {
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
    """Processor example"""

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
            is_valid = main.validate_geojson_format(geojson)
            outputs = {"is_valid": is_valid}

        except Exception:
            raise

        return mimetype, outputs

    def __repr__(self):
        return f'<GeoJsonFormatValidatorProcessor> {self.name}'
