import os
import pytest
from GeodataValidator import main

valid_geojson_format_geometry = {"features":[{"geometry":{"coordinates":[[[9.4001,4.1678],[9.4001,4.1562],[9.4117,4.1562],[9.4117,4.1677],[9.4001,4.1678]]],"type":"Polygon"},"properties":{},"type":"Feature"}],"type":"FeatureCollection"}
invalid_geojson_format = {"type":"Foo", "features":[{"geometry":{"coordinates":[[[9.4001,4.1678],[9.4001,4.1562],[9.4117,4.1562],[9.4117,4.1677],[9.4001,4.1678]]],"type":"Polygon"},"properties":{},"type":"Feature"}]}
invalid_geojson_geometry = {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"coordinates":[[[9.4001,4.1678],[9.4001,4.1562],[9.4117,4.1562],[9.4043,4.1603],[9.4040,4.1555],[9.4001,4.1678]]],"type":"Polygon"}}]}

def test__valid_geosjon_format():
    is_valid = main.validate_geojson_format(valid_geojson_format_geometry)
    assert is_valid == True

def test__valid_geosjon_geometry():
    is_valid = main.validate_geojson_geometry(valid_geojson_format_geometry)
    assert is_valid == True

def test__invalid_geosjon_format():
    is_valid = main.validate_geojson_format(invalid_geojson_format)
    assert is_valid == False

def test__invalid_geosjon_geometry():
    is_valid = main.validate_geojson_geometry(invalid_geojson_geometry)
    assert is_valid == False