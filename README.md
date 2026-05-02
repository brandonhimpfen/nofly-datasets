# nofly-datasets

No-fly zones datasets and loaders in GeoJSON format.

This repository provides a small, source-traceable dataset package for restricted/no-fly airspace data, plus loaders for pulling larger operational datasets from public aviation data services.

## Included datasets

| Path | Source | Coverage | Format |
|---|---|---:|---|
| `data/us/dc/no-fly-zones-p56.geojson` | District of Columbia / National Geospatial-Intelligence Agency dataset distributed through data.gov | P-56A and P-56B restricted flight areas in Washington, DC | GeoJSON |

## Loadable datasets

The repository also includes loaders for larger public datasets that are better fetched on demand instead of committed directly.

| Loader | Source | Notes |
|---|---|---|
| `nofly_datasets.faa_uas_facility_map` | FAA UAS Facility Map ArcGIS FeatureServer | Fetches FAA UAS Facility Map polygons as GeoJSON, including ceiling, airport, airspace, and LAANC fields. |

## Important limitations

This repository is a data engineering resource, not an aviation authority. Do not use it as the sole source for flight planning, authorization, compliance, or safety decisions.

No-fly, restricted, controlled, temporary, and authorization-based airspace can change. Always verify against the official aviation authority, current NOTAMs, and approved flight planning tools before operating an aircraft or UAS.

## Quick start

```bash
python -m pip install -e .
python -m nofly_datasets validate data/us/dc/no-fly-zones-p56.geojson
```

Fetch FAA UAS Facility Map data into GeoJSON:

```bash
python -m nofly_datasets fetch-faa-uas-facility-map \
  --where "CEILING = 0" \
  --limit 2000 \
  --output data/us/faa/uas-facility-map-zero-ceiling.geojson
```

Fetch a bounded area:

```bash
python -m nofly_datasets fetch-faa-uas-facility-map \
  --bbox -77.20 38.75 -76.85 39.05 \
  --limit 2000 \
  --output data/us/faa/uas-facility-map-dc.geojson
```

## Data policy

- No synthetic airspace geometry is included.
- Every committed dataset must include source metadata.
- Large operational datasets should be fetched through loaders and stored as generated artifacts.
- Source attribution must remain attached to derived files.

## Repository structure

```text
data/                 GeoJSON datasets
nofly_datasets/       Python loaders and validation tools
scripts/              Convenience scripts
docs/                 Source notes and schema documentation
tests/                Basic validation tests
```

## License

Code is released under the MIT License.

Dataset licensing follows the original source. The included DC No Fly Zones dataset is listed by data.gov as Creative Commons Attribution. See `NOTICE.md` and `docs/sources.md`.
