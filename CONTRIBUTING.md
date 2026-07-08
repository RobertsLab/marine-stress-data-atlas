# Contributing to the Marine Stress Data Atlas

Thanks for helping build the catalog! One good contribution = **one dataset**:
a new row in the CSV plus a short dataset card. You do **not** need to write
code, install anything, or process sequencing data — and you do **not** need to
know git. Everything can be done from your web browser.

---

## Pick how you want to contribute

| Path | What you do | Git / install needed? | Best for |
|---|---|---|---|
| **A — Submit an issue** | Fill in a short web form; a curator adds the dataset for you | None | First-timers, or if you just found a dataset and want to hand it off |
| **B — Edit in your browser** | Edit the files on GitHub's website; it opens the pull request for you | None | Most students — a bit more involved, full credit as author |
| **C — Local git** | Clone the repo and work on your own computer | Git + Python | People already comfortable with the command line |

If you're not sure, start with **Path A**. You can always graduate to B or C
later.

---

## Path A — Submit a dataset (easiest, no git)

1. Go to the **[Issues](../../issues)** tab and click **New issue**.
2. Choose **"Add a dataset"** and fill in the form (accession, species,
   stressor, etc. — dropdowns are provided for the standardized fields).
3. Submit. A curator turns your submission into a catalog row and a dataset
   card, and credits you.

That's it — no files to edit. Only submit datasets whose data are **publicly
downloadable now** (see [the public-data rule](#confirm-the-data-are-public)).

---

## Path B — Add it yourself in the browser (recommended)

GitHub lets you edit files right on the website. When you make your first edit,
GitHub automatically creates your own copy of the project (a "fork") and, at the
end, opens the pull request for you. Nothing to install.

### 1. Find a dataset and confirm it's public

Good places to search:

- **Google Scholar / PubMed** — find the paper, then look for a "Data
  availability" statement.
- **NCBI GEO** <https://www.ncbi.nlm.nih.gov/geo/> — expression/methylation series (`GSE…`).
- **NCBI SRA / BioProject** <https://www.ncbi.nlm.nih.gov/sra> — raw reads (`SRP…`, `PRJNA…`).
- **EBI ENA** <https://www.ebi.ac.uk/ena> — raw reads (`PRJEB…`).
- **PRIDE** (proteomics), **MetaboLights** / **Metabolomics Workbench** (metabolomics).

<a id="confirm-the-data-are-public"></a>
**Rule:** only add datasets whose data are *publicly downloadable now*. If a
record says "available upon request" or is embargoed, skip it (or add it with
`has_raw_data = unknown` and a note).

### 2. Add a row to the catalog

1. Open [`data/dataset_catalog.csv`](data/dataset_catalog.csv) on GitHub.
2. Click the **pencil ✏️ (Edit this file)** button. GitHub will offer to
   **fork the repository** — click the green button to make your own copy.
3. Scroll to the bottom and add your dataset as **one new line**.

The 21 columns, in order, are:

```
dataset_id, accession, title, species, common_name, life_stage, stressor,
stressor_level, exposure_duration, tissue, omics_type, platform, sample_size,
location, publication_year, publication_doi, data_repository, has_raw_data,
notes, curator, status
```

A completed row looks like this (copy it and replace the values):

```
4,GSE201234,Hypoxia response in eastern oyster gill,Crassostrea virginica,eastern oyster,adult,hypoxia,2 mg/L DO,7 days,gill,RNA-seq,Illumina,20,Chesapeake Bay USA,2023,10.1234/example,GEO,yes,"Control, moderate, and severe hypoxia groups",yourhandle,proposed
```

Then check each value against these rules:

- Give the new row the next unused `dataset_id` (largest existing + 1).
- Fill every column. Use `NA` if a value truly doesn't apply or can't be found.
- For the controlled fields — `stressor`, `life_stage`, `omics_type`,
  `data_repository`, `has_raw_data`, `status` — use a term from
  [`data/controlled_vocabularies.csv`](data/controlled_vocabularies.csv). If your
  dataset needs a term that doesn't exist yet, add it to that file too and
  mention it in your pull-request description.
- If any field contains a comma, wrap the value in double quotes:
  `"Includes control, heat, and recovery groups"`.
- Set `status = proposed` for a new row. A reviewer changes it to `reviewed`
  after checking.

Full field reference is in the [README](README.md#the-catalog-fields).

### 3. Add a dataset card

1. Open the [`dataset_cards/`](dataset_cards/) folder on GitHub and click
   **Add file → Create new file**.
2. Name the file `<accession>.md` (e.g. `GSE201234.md`).
3. Open [`templates/dataset_card_template.md`](templates/dataset_card_template.md)
   in another tab, copy its contents into your new file, and fill it in.

The card captures the details that don't fit in a single CSV row: treatment
groups, replicate counts, file types, reference genome, and access links. Keep
the `dataset_id` in the card identical to the CSV row.

### 4. Propose your changes

After each edit, click **Commit changes** (a short message like
`Add GSE201234` is fine). When you've added both the row and the card, GitHub
shows a **Compare & pull request** button — click it, confirm the checklist in
the pull-request template, and submit.

A second contributor reviews it, spot-checks the accession, and merges. You
don't need to run any validation yourself — a maintainer (and an automated
check) will do that.

---

## Path C — Local git workflow (advanced)

If you're comfortable with the command line:

```bash
git clone https://github.com/RobertsLab/marine-stress-data-atlas.git
cd marine-stress-data-atlas
git checkout -b add-<accession>
```

Edit `data/dataset_catalog.csv` (in a **plain-text editor** — VS Code, nano,
etc., *not* Excel or Numbers, which can silently reformat quotes and dates) and
create `dataset_cards/<accession>.md` from the template:

```bash
cp templates/dataset_card_template.md dataset_cards/GSE201234.md
```

Validate before you push:

```bash
python scripts/validate_catalog.py
```

This checks that the CSV parses, `dataset_id`s are unique, controlled fields use
allowed vocabulary, and every non-example row has a matching card. Fix anything
it flags, then commit both files together and open a pull request:

```bash
git add data/dataset_catalog.csv dataset_cards/GSE201234.md
git commit -m "Add GSE201234 (C. virginica hypoxia RNA-seq)"
git push -u origin add-<accession>
```

---

## Task levels

However you contribute, tasks come in three depths:

| Level | What you do | Time |
|---|---|---|
| **1 — Find** | Add basic metadata for one paper/dataset | 20–30 min |
| **2 — Verify** | Confirm accession, sample size, treatments, tissue, repository | 30–45 min |
| **3 — Curate** | Write a full dataset card + standardized stressor terms | 45–90 min |

Browse the [issues](../../issues) for open tasks — e.g. *"Find 5 oyster
heat-stress RNA-seq datasets"* or *"Verify metadata for coral hypoxia
experiments"* — and comment to claim one, or just start from a paper you know.

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
