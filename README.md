## DATA-BI Projet Spé 2 — Camelyon17 (WILDS)

This repository contains notebooks and resources for a multimodal / histopathology project based on the Camelyon17 dataset from WILDS.

**Important**: you **must** run `get_dataset.py` **before** any other script or notebook.  
It downloads the dataset to the local `data/` folder and prepares the files the notebooks expect.

---

## Contents

- `get_dataset.py` — downloads Camelyon17 from WILDS into `../data`
- `AED.ipynb` — exploratory / analysis notebook
- `training.ipynb` — model training notebook
- `Eval.ipynb` — evaluation notebook
- `ETHAN-AED.ipynb` — Ethan's short exploratory / analysis notebook
- `multimodal_camelyon_model.pth` — saved model weights
- `MAELIO_projet_2_camelyon.ipynb` — Maelio's project notebook

---

## Prerequisites

- Python 3.9+ (recommended)
- `pip` and a virtual environment (optional but recommended)
- Enough disk space for the dataset download

Key dependency used to fetch the dataset:
- `wilds`

---

## Setup

1) Create and activate a virtual environment (optional)
```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies
```bash
pip install wilds
```

---

## Download the dataset (required first step)

Run this **before** any notebook:
```bash
python get_dataset.py
```

This will:
- download Camelyon17 via WILDS
- place the files under `../data`
- print the number of patches loaded

If you skip this step, the notebooks will fail because the dataset isn’t present.

---

## Run the notebooks

After the dataset is downloaded, open and run the notebooks in any order:
- `AED.ipynb`
- `training.ipynb`
- `Eval.ipynb`
- `ETHAN-AED.ipynb`
- `MAELIO_projet_2_camelyon.ipynb`

You may need to adjust paths in the notebooks.

---

## Notes

- The dataset is stored in `../data` relative to this project directory.
- The model weights file `multimodal_camelyon_model.pth` is provided for evaluation or fine‑tuning.
