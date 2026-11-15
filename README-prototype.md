# Reproducible baseline

The prototype is explicitly **new work** and uses fictional records from `data/synthetic_customers.csv`. It is intended as a minimal demonstration of the governance and integration concerns raised in the original study.

Run locally using **Python 3.10+** and no third-party packages:

```bash
python src/mdm_demo.py
python -m unittest discover -s tests -v
```

The system normalizes email addresses, groups exact matching identifiers, favors CRM for display names, tracks all contributing source records, and reports descriptive synthetic-data metrics. It is *not* a production MDM service, a distributed federation engine, or an ML model. Exact-email matching can miss real duplicates and is inappropriate as an unrestricted person-matching rule.
