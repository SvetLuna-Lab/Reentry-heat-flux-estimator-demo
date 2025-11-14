# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- (placeholder) Add radiative heating estimate (Gee–Sutton extension).
- (placeholder) Add altitude-dependent entry profile integration.

### Changed
- (placeholder) Expose unit settings and constants via CLI.

### Fixed
- (placeholder) Guard against invalid CSV rows (NaNs / negatives).

---

## [0.1.0] - 2025-11-14
### Added
- Initial repository skeleton: `src/`, `tests/`, `figures/`, `data/outputs/`.
- Physics models:
  - `src/models.py` — Sutton–Graves stagnation heat flux, ballistic coefficient, peak g-load estimate.
  - `src/atmosphere.py` — exponential density model.
  - `src/run_cases.py` — CSV → CSV batch runner (writes `data/outputs/sample_cases_results.csv`).
- Tests:
  - `tests/test_models.py`, `tests/test_atmosphere.py`.
- Data:
  - `data/sample_cases.csv` with example entry cases.
- Docs:
  - Minimal `README.md` with quick start.
- CI/Dev:
  - `requirements.txt` (pytest only), `.gitignore`, `figures/.gitkeep`.

### Changed
- N/A (initial release)

### Fixed
- N/A (initial release)

[Unreleased]: https://github.com/<ORG_OR_USER>/reentry-heat-flux-estimator-demo/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/<ORG_OR_USER>/reentry-heat-flux-estimator-demo/releases/tag/v0.1.0
