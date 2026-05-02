import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

from .geojson import validate_feature_collection, write_geojson

SERVICE_URL = "https://services6.arcgis.com/ssFJjBXIUyZDrSYZ/arcgis/rest/services/FAA_UAS_FacilityMap_Data/FeatureServer/0/query"
SOURCE_URL = "https://services6.arcgis.com/ssFJjBXIUyZDrSYZ/arcgis/rest/services/FAA_UAS_FacilityMap_Data/FeatureServer/0"


def fetch_faa_uas_facility_map(
    output: str | Path,
    where: str = "1=1",
    bbox: tuple[float, float, float, float] | None = None,
    limit: int = 2000,
    offset: int = 0,
) -> dict:
    params = {
        "where": where,
        "outFields": "*",
        "returnGeometry": "true",
        "f": "geojson",
        "resultOffset": str(offset),
        "resultRecordCount": str(limit),
        "outSR": "4326",
    }
    if bbox is not None:
        xmin, ymin, xmax, ymax = bbox
        params.update({
            "geometry": f"{xmin},{ymin},{xmax},{ymax}",
            "geometryType": "esriGeometryEnvelope",
            "inSR": "4326",
            "spatialRel": "esriSpatialRelIntersects",
        })

    url = SERVICE_URL + "?" + urlencode(params)
    with urlopen(url, timeout=60) as response:
        data = json.loads(response.read().decode("utf-8"))

    validate_feature_collection(data)
    for feature in data.get("features", []):
        props = feature.setdefault("properties", {})
        props.setdefault("source", "Federal Aviation Administration UAS Facility Map Data")
        props.setdefault("source_url", SOURCE_URL)

    write_geojson(data, output)
    return data
