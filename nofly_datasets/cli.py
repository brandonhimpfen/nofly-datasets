import argparse
from pathlib import Path

from .faa_uas_facility_map import fetch_faa_uas_facility_map
from .geojson import load_geojson


def main() -> None:
    parser = argparse.ArgumentParser(prog="nofly-datasets")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="Validate a GeoJSON FeatureCollection")
    validate.add_argument("path")

    fetch = sub.add_parser("fetch-faa-uas-facility-map", help="Fetch FAA UAS Facility Map GeoJSON")
    fetch.add_argument("--output", required=True)
    fetch.add_argument("--where", default="1=1")
    fetch.add_argument("--limit", type=int, default=2000)
    fetch.add_argument("--offset", type=int, default=0)
    fetch.add_argument("--bbox", nargs=4, type=float, metavar=("XMIN", "YMIN", "XMAX", "YMAX"))

    args = parser.parse_args()

    if args.command == "validate":
        data = load_geojson(Path(args.path))
        print(f"valid GeoJSON FeatureCollection: {len(data['features'])} features")
        return

    if args.command == "fetch-faa-uas-facility-map":
        data = fetch_faa_uas_facility_map(
            output=args.output,
            where=args.where,
            bbox=tuple(args.bbox) if args.bbox else None,
            limit=args.limit,
            offset=args.offset,
        )
        print(f"wrote {len(data['features'])} features to {args.output}")


if __name__ == "__main__":
    main()
