#!/bin/bash

cd /home/dougchallener/cdcflu

SINCE=$(date -d '90 days ago' +%Y-%m-%d)

curl -s "https://data.cdc.gov/resource/ymmh-divb.csv?\$where=sample_collect_date>'${SINCE}'&\$limit=50000" \
  -o wastewater_flu_a.csv

git add -A
git diff --cached --quiet || git commit -m "auto: CDC flu update $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git push origin main
