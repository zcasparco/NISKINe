Processing and analysis of data from three moorings as part of NISKINe in the Iceland Basin
======
mplniw repository contains all basic processing codes.

Data_processing contains processing to obtain filtered velocity datasets.



# Near‑Inertial Waves & Mesoscale Interactions  
_A toolbox & analysis suite for observations and ROMS simulations_

---

## Project overview
This repository supports an ongoing study of **near‑inertial waves (NIWs)** and their interactions with mesoscale dynamics in the Iceland Basin in the context othe NISKINe project.  Our goals are to

* map the vertical distribution of **near‑inertial kinetic energy (NIKE)** and quantify its dependence on **mesoscale vorticity**,  
* diagnose **energy transfers** between the NIW frequency band and mesoscale eddies, and  
* evaluate how well these **energy transfers** can be estimated from only three moorings, using an idealised **ROMS** simulation for ground truth.

Core analysis code lives in a small, purpose‑built library, **`mplniw`**, while Jupyter notebooks in three directories present main results.

---

## Repository layout

```text
.
├── mplniw/               # Core Python package: filtering, spectra, transfers, plotting helpers
│   ├── __init__.py
│   ├── filters.py
│   ├── transfers.py
│   └── …                 # etc.
│
├── Data_processing/      # Notebooks that clean, interpolate & band‑pass mooring observations
│   ├── 01_load_and_qc.ipynb
│   ├── 02_interpolate.ipynb
│   └── 03_bandpass_filter.ipynb
│
├── Diagnostics/          # Notebooks that compute diagnostics from the processed data
│   ├── 10_vorticity_maps.ipynb
│   ├── 20_nike_climatology.ipynb
│   ├── 30_energy_transfers.ipynb
│   └── …                 # additional diagnostics
│
├── ROMS/                 # Notebooks & scripts that analyse the idealised ROMS simulation
│   ├── 00_setup_sim.ipynb
│   ├── 40_three_mooring_beta_method.ipynb
│   └── 50_validation_vs_truth.ipynb
│
├── environment.yml       # Conda environment (preferred) with pinned versions
├── requirements.txt      # Same packages in pip format
└── README.md             # You are here


Installation
================


Download the repository:
```
git clone https://github.com/zcasparco/NISKINe.git
```

Data

Mooring observations (netCDF) are stored externally to keep the repository lightweight. Data are not yet available to download.





