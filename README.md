# Reentry-heat-flux-estimator-demo

Stagnation-point **convective heat flux** via **Sutton–Graves**, plus **ballistic coefficient** and a rough **peak g-load** estimate.  
Includes a simple exponential atmosphere model and optional plotting. Python **3.10+**.

---

## Repository structure

```text
reentry-heat-flux-estimator-demo/
├─ src/
│  ├─ __init__.py
│  ├─ models.py          # Sutton–Graves q̇, ballistic coefficient, peak g-load
│  ├─ atmosphere.py      # exponential density model (ISA-like)
│  ├─ run_cases.py       # CSV → CSV batch runner
│  └─ plot_profiles.py   # optional: q̇ vs velocity, q̇ vs density (figures/)
├─ data/
│  ├─ sample_cases.csv   # v_entry_mps,rho_kgm3,Rn_m,k_const,mass_kg,Cd,A_m2
│  └─ outputs/           # results (CSV)
├─ tests/
│  ├─ __init__.py
│  ├─ test_models.py
│  └─ test_atmosphere.py
├─ figures/
│  └─ .gitkeep           # keep folder for plots
├─ README.md
├─ requirements.txt      # tests only: pytest, pytest-cov
├─ requirements-dev.txt  # optional: matplotlib for plots
├─ .gitignore
└─ CHANGELOG.md



Requirements

Python 3.10+

Runtime: standard library only

Tests:

pip install -r requirements.txt


Dev/plots (optional):

pip install -r requirements-dev.txt


Data schema (data/sample_cases.csv)

CSV columns (SI units):

v_entry_mps,rho_kgm3,Rn_m,k_const,mass_kg,Cd,A_m2


v_entry_mps — entry velocity, m/s

rho_kgm3 — freestream density, kg/m³

Rn_m — nose radius, m

k_const — Sutton–Graves constant (Earth ≈ 1.83e-4)

mass_kg — vehicle mass, kg

Cd — drag coefficient (unitless)

A_m2 — reference area, m²


Example

v_entry_mps,rho_kgm3,Rn_m,k_const,mass_kg,Cd,A_m2
7800,0.02,0.5,1.83e-4,1200,1.2,1.8
7500,0.03,0.3,1.83e-4,900,1.4,1.2
7000,0.04,0.7,1.83e-4,1100,1.3,2.0


Quick start
1) Run unit tests

pip install -r requirements.txt
pytest -q


2) Batch evaluate cases (CSV → CSV)

Runs src/run_cases.py on data/sample_cases.csv and writes results to data/outputs/sample_cases_results.csv.

python -m src.run_cases
# Output:
# data/outputs/sample_cases_results.csv


Output columns added:

qdot_Wm2 — stagnation heat flux (W/m²)

beta_kgm2 — ballistic coefficient (kg/m²)

g_peak — rough peak g-load (g₀)


3) (Optional) Plot heating profiles

Generates two figures in figures/ using matplotlib.

pip install -r requirements-dev.txt
python -m src.plot_profiles
# figures/qdot_vs_velocity.png
# figures/qdot_vs_density.png


What’s inside

src/models.py

sutton_graves_heat_flux(case) → q̇ = k * sqrt(ρ / Rn) * v^3 (W/m²)

ballistic_coefficient(case) → β = m / (Cd * A) (kg/m²)

peak_g_load_estimate(v_entry) → order-of-magnitude g-load (g₀)

src/atmosphere.py

rho_exponential(h) → ρ = ρ₀ * exp(-h/H)

src/run_cases.py

Batch CSV runner (reads data/sample_cases.csv, writes data/outputs/*.csv)

src/plot_profiles.py (optional)

q̇ vs velocity (ρ, Rn fixed)

q̇ vs density (v, Rn fixed)


Assumptions & scope

Idealized, order-of-magnitude estimates for Earth entry

Convective heating only (radiation not included)

Constants (k_const, Cd) are scenario-dependent; tune for your vehicle

For design, use CFD/arc-jet data and validated correlations


Console output example

$ python -m src.run_cases
# writes: data/outputs/sample_cases_results.csv

$ python -m src.plot_profiles
Saved figures:
 - figures/qdot_vs_velocity.png
 - figures/qdot_vs_density.png


Versioning

We follow Semantic Versioning. See CHANGELOG.md
.
Initial release: v0.1.0.


License

Add a LICENSE file (e.g., MIT) if you plan to open source and reference it here.

