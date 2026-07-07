# Contributing to the Marine Stress Data Atlas

Thanks for helping build the catalog! One good contribution = **one dataset**:
a new row in the CSV plus a short dataset card. This guide walks you through it.
You do **not** need to write code or process any sequencing data.

---

## 1. Claim a task

Browse the [issues](../../issues) and comment "I'll take this" on one that's
unclaimed, or just start from a paper you already know. Typical tasks:

- *Find 5 publicly available oyster heat-stress RNA-seq datasets*
- *Add datasets for sea stars exposed to disease or wasting syndrome*
- *Curate ocean-acidification methylation datasets in bivalves*
- *Verify metadata for coral hypoxia experiments*
- *Find public metabolomics datasets from shellfish aquaculture studies*

### Task levels

| Level | What you do | Time |
|---|---|---|
| **1 — Find** | Add basic metadata for one paper/dataset | 20–30 min |
| **2 — Verify** | Confirm accession, sample size, treatments, tissue, repository | 30–45 min |
| **3 — Curate** | Write a full dataset card + standardized stressor terms | 45–90 min |

---

## 2. Find a dataset and confirm it's public

Good places to search:

- **Google Scholar / PubMed** — find the paper, then look for a "Data
  availability" statement.
- **NCBI GEO** <https://www.ncbi.nlm.nih.gov/geo/> — expression/methylation series (`GSE…`).
- **NCBI SRA / BioProject** <https://www.ncbi.nlm.nih.gov/sra> — raw reads (`SRP…`, `PRJNA…`).
- **EBI ENA** <https://www.ebi.ac.uk/ena> — raw reads (`PRJEB…`).
- **PRIDE** (proteomics), **MetaboLights** / **Metabolomics Workbench** (metabolomics).

**Rule:** only add datasets whose data are *publicly downloadable now*. If a
record says "available upon request" or is embargoed, skip it (or add it with
`has_raw_data = unknown` and a note).

---

## 3. Add a row to `data/dataset_catalog.csv`

- Give the new row the next unused `dataset_id` (largest existing + 1).
- Fill every column. Use `NA` if a value truly doesn't apply or can't be found.
- For the controlled fields — `stressor`, `life_stage`, `omics_type`,
  `data_repository`, `has_raw_data`, `status` — use a term from
  [`data/controlled_vocabularies.csv`](data/controlled_vocabularies.csv). If your
  dataset needs a term that doesn't exist yet, add it to that file in the same PR
  and mention it in your PR description.
- If any field contains a comma, wrap the value in double quotes:
  `"Includes control, heat, and recovery groups"`.
- Set `status = proposed` for a new row. A reviewer changes it to `reviewed`
  after checking.

Field reference is in the [README](README.md#the-catalog-fields).

---

## 4. Create a dataset card

Copy the template and rename it to the accession:

```bash
cp templates/dataset_card_template.md dataset_cards/GSE123456.md
```

Fill in the table and the experimental-design section. The card is where you
capture the details that don't fit in a single CSV row: treatment groups,
replicate counts, file types, reference genome, and access links. Keep the
`dataset_id` in the card identical to the CSV row.

---

## 5. Validate (optional but appreciated)

```bash
python scripts/validate_catalog.py
```

This checks that the CSV parses, `dataset_id`s are unique, controlled fields use
allowed vocabulary, and every non-example row has a matching card in
`dataset_cards/`. Fix anything it flags.

---

## 6. Open a pull request

1. Create a branch: `git checkout -b add-<accession>`.
2. Commit the CSV change and the new card together.
3. Push and open a PR. Use a title like `Add GSE123456 (C. gigas heat RNA-seq)`.
4. The PR template will ask you to confirm the data are public and the row validates.

A second contributor reviews the PR, spot-checks the accession, and merges.

---

## Style conventions

- **Species:** full Latin binomial, genus capitalized: `Crassostrea gigas`.
- **Stressor level:** as reported, with units: `30 C`, `pH 7.6`, `1 mg/L Cu`.
- **Duration:** number + unit: `5 days`, `72 hours`, `chronic`.
- **Tissue:** lowercase, underscores for multi-word: `whole_organism`, `digestive_gland`.
- **One dataset per row and per card.** If one paper deposited two separate
  accessions, make two rows.
- **DOIs** as bare identifiers (`10.1234/abcd`), not full URLs.

Questions? Open an issue with the `question` label. Happy curating!
