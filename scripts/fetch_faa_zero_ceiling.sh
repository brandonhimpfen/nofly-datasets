#!/usr/bin/env bash
set -euo pipefail

python -m nofly_datasets fetch-faa-uas-facility-map   --where "CEILING = 0"   --limit 2000   --output data/us/faa/uas-facility-map-zero-ceiling.geojson
