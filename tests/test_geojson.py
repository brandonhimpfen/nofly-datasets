from pathlib import Path

from nofly_datasets.geojson import load_geojson


def test_dc_p56_dataset_is_valid():
    path = Path("data/us/dc/no-fly-zones-p56.geojson")
    data = load_geojson(path)
    assert data["type"] == "FeatureCollection"
    assert len(data["features"]) == 2
    assert {f["properties"]["NAME"] for f in data["features"]} == {"P56A", "P56B"}
