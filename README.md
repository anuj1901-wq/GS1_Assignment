# GS1 Customer Intelligence — aggregate-only dashboard

The dashboard uses precomputed aggregate exports derived from the supplied Snowflake SQL. No company name, GCP, company ID, raw CSV or Snowflake credential is included.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Snowflake workflow

Run and validate the Snowflake analysis views, export the aggregate results, and update only the seven CSVs in `data/`. The `build_exports.py` helper regenerates those sanitized CSVs from the seven local Snowflake exports if placed in the parent folder under the exact filenames used in that script. Do not publish the source exports if they contain customer-level data.

## Public deployment

Push ONLY this `gs1_dashboard` folder to GitHub (or an equivalent project folder). On Streamlit Community Cloud choose the repository and `app.py` as the entry point. The URL is supplied by Streamlit after successful deployment. This app does not require Snowflake credentials. Review all repository files before making the repository public.

## Methodology limitations

As of 2026-10-20. Engagement uses GTIN creation recency, not ongoing barcode utility. Expiry results use last creation timestamp vs recorded expiry and do not establish unauthorized access. Cohort plot omits cohorts with fewer than 20 GCPs; plan-specific expiry plot omits groups with fewer than 10 expired GCPs. Priority scores are heuristics without labeled churn outcomes. Group filters are intentionally omitted to prevent small-cell discovery.
