import csv
import os
from .models import ReentryCase, sutton_graves_heat_flux, ballistic_coefficient, peak_g_load_estimate

def run_csv(in_csv: str, out_csv: str) -> None:
    os.makedirs(os.path.dirname(out_csv) or ".", exist_ok=True)
    rows_out = []
    with open(in_csv, "r", encoding="utf-8") as f:
        rd = csv.DictReader(f)
        for r in rd:
            case = ReentryCase(
                v_mps=float(r["v_entry_mps"]),
                rho=float(r["rho_kgm3"]),
                Rn=float(r["Rn_m"]),
                k=float(r.get("k_const", 1.83e-4)),
                mass=float(r.get("mass_kg", 1000.0)),
                Cd=float(r.get("Cd", 1.2)),
                area=float(r.get("A_m2", 1.0)),
            )
            q = sutton_graves_heat_flux(case)
            beta = ballistic_coefficient(case)
            gpk = peak_g_load_estimate(case.v_mps)
            rows_out.append({
                **r,
                "qdot_Wm2": f"{q:.3e}",
                "beta_kgm2": f"{beta:.1f}",
                "g_peak": f"{gpk:.2f}",
            })
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
        wr.writeheader()
        wr.writerows(rows_out)

if __name__ == "__main__":
    run_csv("data/sample_cases.csv", "data/outputs/sample_cases_results.csv")
