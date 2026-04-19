# Information Dynamics – p_ID Extraction from Four Particle Physics Experiments

This repository contains a Python script that extracts the **information purity** p_ID from publicly available data of four independent experiments:
1. Hyperon semileptonic decay Lambda -> p mu- anti-nu_mu (BESIII 2021)
2. Reactor neutrino oscillation Delta m^2_21 (KamLAND + JUNO 2025) – used as calibration anchor
3. X17 resonance branching ratio (Atomki 2020)
4. Muon g-2 anomalous magnetic moment (Fermilab 2025)

All extractions consistently give p_ID ≈ 1, indicating that the information field resides in an **information‑superconducting state**. This single‑parameter description unifies strong and weak interactions as internal rotational symmetries of the information field.

---

## 1. Purpose

The script provides a transparent, reproducible calculation of the information purity p_ID from each experiment. No free parameters are fitted – each value is directly derived from published measurements and standard model predictions (or a conservative anchor assumption for the reactor neutrino case). The results support the theoretical framework developed in the accompanying paper.

---

## 2. Experiments and Data Sources

| Experiment | Observable | Reference | Role |
|------------|------------|-----------|------|
| Hyperon decay | Branching fraction B_exp = (1.48 +/- 0.23) x 10^-4 | BESIII, Phys. Rev. Lett. 127, 121802 (2021) | Inversion |
| Reactor neutrino | Delta m^2_21 = (7.48 +/- 0.10) x 10^-5 eV^2 | JUNO, arXiv:2511.14593 (2025) | **Calibration anchor** (p_ID = 1) |
| X17 resonance | B_X = (6 +/- 1) x 10^-6 | Krasznahorkay et al., EPJ Web Conf. 232, 04005 (2020) | Inversion (p_ID = 1 - B_X) |
| Muon g-2 | a_mu_exp = 0.001165920705, a_mu_SM = 0.00116592033 | Fermilab, arXiv:2506.03069 (2025); 2025 White Paper | Inversion (p_ID = a_mu_exp / a_mu_SM) |

> **Note:** The reactor neutrino measurement is taken as the information‑superconducting anchor (p_ID = 1) because it occurs in a short‑baseline vacuum environment, which is the closest realization of an ideal coherent state.

---

## 3. Requirements

- Python 3.6+
- Required packages: numpy

Install with:
```bash
pip install numpy
```

---

## 4. Usage

Clone the repository and run the script:

```bash
git clone https://github.com/hkaiopen/InformationDynamics_particlephysics.git
cd InformationDynamics_particlephysics
python pID_extraction_four_experiments.py
```

The script will print the extracted p_ID values with uncertainties and a summary table.

---

## 5. Output Interpretation

- All extracted p_ID values are close to **1**, meaning the information field in these high‑energy or low‑dissipation environments is in an **information‑superconducting state**.
- The reactor neutrino result is not an inversion but a **calibration anchor** – it sets the reference for a perfect information superconductor.
- The hyperon decay and muon g-2 results are consistent with unity within their uncertainties.
- The X17 resonance, with a tiny branching ratio 6 x 10^-6, gives p_ID = 0.999994, showing that even rare collective excitations occur in a nearly perfect coherent environment.

These numbers provide strong phenomenological support for the Information Dynamics framework applied to non‑Abelian gauge fields.

---

## 6. Repository Contents

- `pID_extraction_four_experiments.py` – Main Python script (calculations with error propagation)
- `README.md` – This file
- `Output.txt` – Console output (No plots are generated; results are printed to the console)

---

## 7. License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** (CC BY-NC-SA 4.0).

You are free to **share** and **adapt** the material under the following terms:
- **Attribution** – You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial** – You may not use the material for commercial purposes.
- **ShareAlike** – If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

For commercial use, please contact the authors.

---

## 8. Citation

If you use this code or the results, please cite:

1. **The accompanying research paper (preprint):**  
   > Huang, K., Liu, H., Huang, Z., & Kuang, Q. (2026). *Information Dynamics: Emergence of Non‑Abelian Gauge Fields from Local SU(N) Invariance of a Generalized Ginzburg‑Landau Equation and Phenomenological Consistency with Four Independent Experiments*. Zenodo preprint. (https://doi.org/10.5281/zenodo.19447818)

2. **This software repository:**  
   > Huang, K. (2026). *hkaiopen/InformationDynamics_particlephysics* (Version v1.0) [Computer software]. Zenodo.(https://doi.org/10.5281/zenodo.19448369)

For the reactor neutrino anchor, please also acknowledge the JUNO Collaboration and cite arXiv:2511.14593.

---

*For questions or suggestions, please open an issue or contact the authors.*
