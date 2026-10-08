#!/usr/bin/env python3
"""
Reproducible Data Ingestion Pipeline
Fetches the open data records directly from Generalitat de Catalunya's Socrata API / CSV endpoint:
Transparència Catalunya - Grups de recerca de Catalunya (Dataset ufpk-rk8r)
"""

import os
import urllib.request
import csv
import io

DATASET_CSV_URL = "https://analisi.transparenciacatalunya.cat/api/views/ufpk-rk8r/rows.csv?accessType=DOWNLOAD"

def download_dataset(output_path: str, sample_limit: int = 500):
    print(f"[INGESTION] Fetching dataset from {DATASET_CSV_URL}...")
    req = urllib.request.Request(DATASET_CSV_URL, headers={"User-Agent": "Mozilla/5.0 (AI-Research-Agent)"})
    
    with urllib.request.urlopen(req) as resp:
        data = resp.read().decode("utf-8", errors="replace")
        reader = csv.DictReader(io.StringIO(data))
        fieldnames = reader.fieldnames

        selected_rows = []
        seen_ids = set()
        for row in reader:
            gid = row.get("_id")
            if gid in seen_ids:
                continue
            seen_ids.add(gid)
            selected_rows.append(row)
            if sample_limit and len(selected_rows) >= sample_limit:
                break

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(selected_rows)

        print(f"[INGESTION SUCCESS] Saved {len(selected_rows)} records to {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(base_dir, "data", "catalan_research_groups_sample.csv")
    download_dataset(target_path)
