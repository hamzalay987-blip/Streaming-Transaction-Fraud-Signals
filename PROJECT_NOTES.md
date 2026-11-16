# Project notes: Incremental API-to-Warehouse Ingestion

**Business problem:** API sources may paginate results and deliver updated records, making full reloads expensive and error-prone.

**Design:** Ingest ordered pages, apply versioned records with upsert semantics, and persist the high-watermark.

**Interview discussion:** Explain schema assumptions, late data/duplicate behavior, controls, expected tradeoffs, and what would change at enterprise scale.

**Suggested next feature:** Add sample-sized integration tests or a docker-compose service when the implementation is ready.
