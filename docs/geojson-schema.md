# GeoJSON requirements

Committed dataset files should be valid GeoJSON `FeatureCollection` documents.

Required collection-level fields:

- `type`: `FeatureCollection`
- `features`: array of GeoJSON features

Recommended feature properties:

- `NAME` or `name`
- `source`
- `source_url`
- `retrieved`
- source-specific identifiers such as `OBJECTID`, `GIS_ID`, or `GLOBALID`

Geometry should use WGS 84 longitude/latitude coordinates compatible with standard GeoJSON tooling.
