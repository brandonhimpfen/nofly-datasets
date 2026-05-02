import json
from pathlib import Path
from typing import Any, Dict


def load_geojson(path: str | Path) -> Dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate_feature_collection(data)
    return data


def validate_feature_collection(data: Dict[str, Any]) -> None:
    if data.get("type") != "FeatureCollection":
        raise ValueError("GeoJSON must be a FeatureCollection")
    if not isinstance(data.get("features"), list):
        raise ValueError("GeoJSON FeatureCollection must include a features array")
    for index, feature in enumerate(data["features"]):
        if feature.get("type") != "Feature":
            raise ValueError(f"Feature {index} is not a GeoJSON Feature")
        if "geometry" not in feature:
            raise ValueError(f"Feature {index} is missing geometry")
        if "properties" not in feature:
            raise ValueError(f"Feature {index} is missing properties")


def write_geojson(data: Dict[str, Any], path: str | Path) -> None:
    validate_feature_collection(data)
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + "
", encoding="utf-8")
