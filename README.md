# Marine Stress Data Atlas

A community-curated catalog of **publicly available datasets on marine organisms
exposed to environmental stress** — heat, ocean acidification, disease, hypoxia,
salinity, and pollutants.

Each contribution is small, independent, and data-focused: a student finds one
paper/dataset, verifies the information, adds **one row** to a CSV, and writes a
short **dataset card**. Over time this builds a clean, reusable database the lab
can mine for meta-analyses, reanalysis, and AI/ML training data.

No coding, sequencing analysis, or close coordination required.

---

## What's in here

```
marine-stress-data-atlas/
├── data/
│   ├── dataset_catalog.csv          # one row per dataset — the core table
│   └── controlled_vocabularies.csv  # allowed terms for key fields
├── dataset_cards/                   # one Markdown card per dataset
│   ├── GSE123456.md                 # (example)
│   └── PRJNA123456.md               # (example)
├── templates/
│   └── dataset_card_template.md     # copy this to start a new card
├── scripts/
│   └── validate_catalog.py          # checks the CSV before you open a PR
├── notebooks/
│   └── catalog_summary.ipynb        # coverage summaries & simple charts
├── CONTRIBUTING.md                  # step-by-step contributor guide
└── .github/                         # issue & PR templates
```

> The rows and cards currently in the repo are **examples** (`status = example`,
> fake accessions). Replace them with real datasets as they come in.

## The catalog fields

Every dataset is one row in [`data/dataset_catalog.csv`](data/dataset_catalog.csv):

| Field | Meaning |
|---|---|
| `dataset_id` | Sequential integer, unique per row |
| `accession` | Repository accession (e.g. `GSE123456`, `PRJNA123456`) |
| `title` | Short descriptive title |
| `species` | Latin binomial (e.g. *Crassostrea gigas*) |
| `common_name` | Common name |
| `life_stage` | embryo / larva / juvenile / adult / mixed |
| `stressor` | heat / ocean_acidification / hypoxia / salinity / disease / pollutant / multistressor |
| `stressor_level` | Dose/level as reported (e.g. `30 C`, `pH 7.6`) |
| `exposure_duration` | e.g. `5 days` |
| `tissue` | Tissue or sample type (e.g. gill, mantle, whole_organism) |
| `omics_type` | RNA-seq / WGBS / proteomics / metabolomics / … |
| `platform` | Sequencing/assay platform (e.g. Illumina) |
| `sample_size` | Number of samples/libraries |
| `location` | Collection or study location |
| `publication_year` | Year |
| `publication_doi` | DOI of the associated paper |
| `data_repository` | GEO / SRA / ENA / PRIDE / MetaboLights / … |
| `has_raw_data` | yes / no / unknown |
| `notes` | Free text (caveats, design notes) |
| `curator` | Your name / GitHub handle |
| `status` | proposed / reviewed / example |

Allowed values for the controlled fields live in
[`data/controlled_vocabularies.csv`](data/controlled_vocabularies.csv). For a
worked example of a completed row, see
[section 3 of CONTRIBUTING.md](CONTRIBUTING.md#3-add-a-row-to-datadataset_catalogcsv).

## How to contribute

**No git or coding required — you can do everything in your web browser.**
Pick whichever fits you:

- **Easiest — submit a form.** Open a [new issue](../../issues/new/choose),
  choose **"Add a dataset"**, and fill in the fields. A curator adds it to the
  catalog for you.
- **Do it yourself in the browser.** Edit the files on GitHub's website; it
  forks the project and opens the pull request for you. No software to install.
- **Local git (advanced).** Clone the repo and work from the command line.

The gist either way: find a relevant paper/dataset, confirm the data are
**publicly accessible**, add one row to `data/dataset_catalog.csv`, and add a
matching card in `dataset_cards/`.

Full walkthrough with step-by-step instructions for each path:
**[CONTRIBUTING.md](CONTRIBUTING.md)**.

### Task levels

| Level | Work | Time |
|---|---|---|
| **1 — Find** | Add basic metadata for one paper/dataset | 20–30 min |
| **2 — Verify** | Check accession, sample size, treatments, tissue, repository | 30–45 min |
| **3 — Curate** | Add a detailed dataset card and standardized stressor terms | 45–90 min |

Look for open [issues](../../issues) to claim — e.g. *"Find 5 public oyster
heat-stress RNA-seq datasets"* or *"Verify metadata for coral hypoxia experiments."*

## First milestone

> **Curate 100 public marine environmental-stress datasets** across at least
> **20 species**, each with accession numbers, stressor, tissue, life stage, and
> omics data type.

Progress is easy to check any time:

```bash
python scripts/validate_catalog.py                  # validate the table
jupyter notebook notebooks/catalog_summary.ipynb    # coverage & charts
```

## Why this exists

Once populated, the atlas lets the lab quickly ask questions like:

- Which species have repeated heat-stress RNA-seq datasets?
- Are methylation datasets concentrated in a few taxa?
- Which stressors lack larval-stage data?
- What public data could support cross-species prediction of resilience?

It connects directly to the lab's public-omics / watchtower work, environmental
memory research, and marine multi-omics interests.

## License

Catalog metadata (the CSV files and dataset cards) is released under
[CC0 1.0](LICENSE) — it describes third-party datasets and adds no new
restrictions. Always follow the license of each **underlying** dataset when you
use it.
