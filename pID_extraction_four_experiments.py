"""
================================================================================
Information Dynamics: Extraction of Information Purity from Four Experiments
================================================================================

This script extracts the information purity p_ID from four independent experiments:
1. Hyperon semileptonic decay Λ → p μ⁻ ν̄_μ (BESIII 2021)
2. Reactor neutrino oscillation Δm²₂₁ (KamLAND, JUNO 2025) - used as calibration anchor
3. X17 resonance branching ratio (Atomki 2020)
4. Muon g-2 anomalous magnetic moment (Fermilab 2025)

All data are taken from published literature. See paper for details.
================================================================================
"""

import numpy as np

# =============================================================================
# Experiment 1: Hyperon Semileptonic Decay Λ → p μ⁻ ν̄_μ (BESIII 2021)
# =============================================================================
# Source: BESIII Collaboration, Phys. Rev. Lett. 127, 121802 (2021)
# Link: https://inspirehep.net/literature/1884047
# Data: branching fraction B_exp = (1.48 ± 0.21_stat ± 0.08_syst) × 10⁻⁴
# Note: The result agrees with Standard Model prediction. We take B_SM = B_exp,
#       with a conservative 5% uncertainty.

B_exp = 1.48e-4
err_stat = 0.21e-4
err_syst = 0.08e-4
err_B_exp = np.sqrt(err_stat**2 + err_syst**2)

B_SM = B_exp
err_B_SM = B_SM * 0.05

p_ID_hyperon = B_exp / B_SM
err_p_ID_hyperon = p_ID_hyperon * np.sqrt((err_B_exp/B_exp)**2 + (err_B_SM/B_SM)**2)

print("=" * 70)
print("Experiment 1: Hyperon Semileptonic Decay Λ → p μ⁻ ν̄_μ")
print("=" * 70)
print(f"Data source: BESIII Collaboration, Phys. Rev. Lett. 127, 121802 (2021)")
print(f"Link: https://inspirehep.net/literature/1884047")
print(f"B_exp = ({B_exp:.3e} ± {err_B_exp:.3e})")
print(f"B_SM  = ({B_SM:.3e} ± {err_B_SM:.3e})")
print(f"Extracted p_ID = {p_ID_hyperon:.4f} ± {err_p_ID_hyperon:.4f}\n")

# =============================================================================
# Experiment 2: Reactor Neutrino Oscillation (Calibration Anchor)
# =============================================================================
# Source: Updated global bounds from JUNO results (arXiv:2511.21650)
# Link: https://arxiv.org/abs/2511.21650
# Data: Δm²₂₁ = (7.48 ± 0.10) × 10⁻⁵ eV² (reactor measurement)
# Role: This experiment occurs in a short-baseline vacuum environment,
#       which is assumed to be the information superconductor limit.
#       Therefore we set p_ID = 1 as the calibration anchor.

dm2_reactor = 7.48e-5
err_dm2_reactor = 0.10e-5

# Calibration anchor (assumed perfect information superconductor)
p_ID_reactor = 1.0
err_p_ID_reactor = 0.0

print("=" * 70)
print("Experiment 2: Reactor Neutrino Oscillation (Calibration Anchor)")
print("=" * 70)
print(f"Data source: JUNO Collaboration, arXiv:2511.21650 (2025)")
print(f"Link: https://arxiv.org/abs/2511.21650")
print(f"Δm²₂₁ (reactor) = ({dm2_reactor:.3e} ± {err_dm2_reactor:.3e}) eV²")
print(f"Assumed p_ID = {p_ID_reactor} (information superconductor limit)\n")

# =============================================================================
# Experiment 3: X17 Resonance Branching Ratio (Atomki 2020)
# =============================================================================
# Source: Krasznahorkay et al., EPJ Web Conf. 232, 04005 (2020)
# Link: https://real.mtak.hu/115062/
# Data: B_X = (6 ± 1) × 10⁻⁶ (branching ratio of the 18.15 MeV transition)
# Interpretation: In Information Dynamics, the production probability of
#                a rare collective excitation equals the information impurity (1-p_ID).

B_X = 6.0e-6
err_B_X = 1.0e-6

p_ID_X17 = 1.0 - B_X
err_p_ID_X17 = err_B_X

print("=" * 70)
print("Experiment 3: X17 Resonance (Atomki 2020)")
print("=" * 70)
print(f"Data source: Krasznahorkay et al., EPJ Web Conf. 232, 04005 (2020)")
print(f"Link: https://real.mtak.hu/115062/")
print(f"B_X = ({B_X:.2e} ± {err_B_X:.2e})")
print(f"Extracted p_ID = {p_ID_X17:.6f} ± {err_p_ID_X17:.2e}\n")

# =============================================================================
# Experiment 4: Muon g-2 Anomalous Magnetic Moment (Fermilab 2025)
# =============================================================================
# Source: Fermilab Muon g-2 Collaboration, arXiv:2506.03069 (2025)
# Link: https://arxiv.org/abs/2506.03069
# Data: a_exp = 0.001165920705 ± 0.000000000114(stat) ± 0.000000000091(syst)
#       a_SM  = 0.00116592033 (2025 White Paper, data-driven approach)

a_exp = 0.001165920705
err_stat = 0.000000000114
err_syst = 0.000000000091
err_a_exp = np.sqrt(err_stat**2 + err_syst**2)

a_SM = 0.00116592033
err_a_SM = 5.4e-10   # approx. 540 ppb uncertainty from White Paper 2025

p_ID_g2 = a_exp / a_SM
err_p_ID_g2 = p_ID_g2 * np.sqrt((err_a_exp/a_exp)**2 + (err_a_SM/a_SM)**2)

print("=" * 70)
print("Experiment 4: Muon g-2 Anomalous Magnetic Moment (Fermilab 2025)")
print("=" * 70)
print(f"Data source: Fermilab Muon g-2 Collaboration, arXiv:2506.03069 (2025)")
print(f"Link: https://arxiv.org/abs/2506.03069")
print(f"a_exp = {a_exp:.12f} ± {err_a_exp:.12f}")
print(f"a_SM  = {a_SM:.11f} ± {err_a_SM:.2e}")
print(f"Extracted p_ID = {p_ID_g2:.9f} ± {err_p_ID_g2:.2e}\n")

# =============================================================================
# Summary Table
# =============================================================================
print("=" * 70)
print("Summary of p_ID Extraction")
print("=" * 70)
print(f"{'Experiment':<35} {'p_ID':<20} {'Energy Scale'}")
print("-" * 70)
print(f"{'Hyperon decay Λ→pμν̄':<35} {p_ID_hyperon:.4f} ± {err_p_ID_hyperon:.4f}   ~1 GeV")
print(f"{'Reactor neutrino (calibration)':<35} {p_ID_reactor:<20}   ~MeV")
print(f"{'X17 resonance':<35} {p_ID_X17:.6f} ± {err_p_ID_X17:.2e}   ~10 MeV")
print(f"{'Muon g-2':<35} {p_ID_g2:.9f} ± {err_p_ID_g2:.2e}   ~100 MeV")
print("=" * 70)

# =============================================================================
# Discussion
# =============================================================================
print("\nDiscussion:")
print("All extractions give p_ID ≈ 1 (information superconductor limit).")
print("The reactor neutrino measurement is used as the p_ID = 1 calibration anchor.")
print("Hyperon decay and muon g-2 results are consistent with unity within errors.")
print("X17, with B_X = 6e-6, gives p_ID = 0.999994, showing that even rare")
print("collective excitations occur in a nearly perfect information superconductor.")
print("=" * 70)