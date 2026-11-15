# Research Overview and Critical Appraisal

## Work and provenance

**Title:** *Master Data Management: Business Case and Roadmap for MDM Architecture*  
**Author:** Sujit Adhikari  
**Type:** Academic research-style architectural case study (original course paper; exact completion date unverified)  
**Original length:** 23 pages

This repository preserves an academic proposal written around a hypothetical San Francisco-based omnichannel pet-supply retailer, named **ABC Company**. The hypothetical business is expanding from pet food into additional pet-related products. Its customer, finance, sales, and operations data are distributed across functions.

The original paper asks how an affordable master data management (MDM) program could create reliable shared views and support cross-selling, customer retention, and product-line decisions.

## Problem and proposed approach

The paper argues that MDM is a governance and organizational problem, not merely a technology selection issue. Its principal architectural recommendation is **virtual integration via Data Service Federation (DSF)**, with master-data views made accessible on demand, rather than wholesale duplication into one centralized system. It also outlines:

1. Business case and drivers for product-line expansion.
2. MDM governance responsibilities and key disciplines.
3. Ownership and access considerations.
4. Data-source and domain analysis.
5. Relationships, hierarchies, and entity grouping.
6. An implementation roadmap and management prerequisites.

## Research approach

This is a **literature-informed, design-oriented case proposal**. It synthesizes published MDM and governance concepts into a proposed architecture for a hypothetical enterprise. The paper includes in-text citations and a bibliography in an author-date format. Its format is closer to a research-style case study than a conventional software assignment.

It is **not** an empirical evaluation, peer-reviewed publication, implementation report, or controlled experiment. There is no demonstrated production deployment, prospective impact assessment, or validated cost comparison in the source manuscript.

## Contribution

The defensible contribution is an **integrated business-and-technology decision framework**, bringing together the retailer's business objectives, data governance, master data domains, and phased architectural choice.

## Limitations and future research

- **Hypothetical organization:** The ABC Company case is a constructed scenario, not documented field research.
- **Implementation evidence:** The chosen DSF architecture is proposed, not deployed or benchmarked.
- **Cost comparison:** The source motivates DSF as affordable, but does not give a reproducible financial model comparing alternatives.
- **Entity resolution:** The paper identifies duplicate and inconsistent records as concerns but does not demonstrate measured matching accuracy.
- **Architectural nuance:** Federation can reduce replication, but introduces trade-offs involving availability, source-system performance, latency, lineage, and access-control coordination.
- **Source quality:** The bibliography blends books, technical articles, practitioner material, and web resources. Some entries need bibliographic verification and consistent APA treatment.
- **Contemporary relevance:** Modern links to retrieval-augmented generation (RAG) and knowledge governance are *subsequent interpretations*, not research carried out in the original paper.

## Suggested evaluation design (new work, not part of original manuscript)

A later technical extension could compare source-specific records with a virtual integrated view using a synthetic, documented benchmark. Outcomes should include duplicate rate, precision and recall of entity matching, completeness, consistency, latency, and query correctness. The code and metrics must be reproducible and should not be retroactively attributed to the original study.

## Reading guidance

- [Original manuscript](original-manuscript.md)
- [Reference list](references.md)
- [Modern extension plan](../docs/extension-plan.md)
