# Master Data Management: Business Case and Roadmap for MDM Architecture

**Sujit Adhikari** · Academic research-style case study · Original coursework (completion year not independently verified)

> **Status:** An academic architecture and governance proposal, **not a peer-reviewed journal publication**. The original analysis is preserved in `paper/original-manuscript.md`; subsequent code and research extensions are identified separately.

## Abstract

This project studies how a growing omnichannel pet-products retailer could establish consistent customer, product, and transaction master data across departments while expanding its product lines. The paper frames master data management (MDM) as both an information-architecture and organizational-governance challenge. It recommends a **Data Service Federation** approach to deliver integrated views across heterogeneous systems without requiring wholesale migration. The proposal considers stakeholder ownership, data stewardship, quality controls, domain models, entity relationships, and a staged implementation roadmap.

**Keywords:** master data management, data governance, data federation, entity resolution, enterprise architecture, decision support, data quality.

## Read the paper

- **[Original manuscript — text transcription](paper/original-manuscript.md)**: transcription of the supplied 23-page academic manuscript; formatting, diagrams, and tables in the original Word document may not fully survive text extraction. Original wording is retained where recoverable.
- **[Research overview and limitations](paper/research-overview.md)**: scope, method, contributions, and boundary between conceptual architecture and evaluated software.
- **[References and provenance](paper/references.md)**: references transcribed from the original paper; incomplete citations are flagged rather than invented.
- **[Research-to-implementation extension](docs/extension-plan.md)**: proposed modern validation work, clearly separated from the original study.

## Scope and research integrity

The paper investigates a **hypothetical ABC Company** scenario. The recommended architecture is a **proposal**, not evidence that the enterprise system was deployed or that measurable quality gains were achieved. A companion implementation may be added as a **2026 extension**, using synthetic data and reproducible tests; any outcomes will be reported only after execution and validation.

The repository does not claim university sponsorship, external peer review, publication, or empirical outcomes unsupported by the supplied manuscript.

## Relevance

This case study documents early work on data stewardship, reliable shared knowledge, heterogeneous data integration, and decision-support systems. Those interests connect conceptually to modern retrieval-augmented systems, knowledge governance, and trustworthy information pipelines, but the original project **does not experiment with LLMs or RAG**.

## Author

**Sujit Adhikari**

## Citation

See [CITATION.cff](CITATION.cff) for suggested citation metadata. The year is deliberately marked as unverified until the coursework date is confirmed.

## License

No explicit reuse license is granted for the original manuscript at present. Original text and cited third-party material remain subject to their respective rights. Proposed implementation code can be separately licensed if added.
