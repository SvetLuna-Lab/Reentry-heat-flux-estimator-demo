"""
Plot simple reentry heating profiles using the Sutton–Graves correlation.

Outputs (saved to ./figures/):
- qdot_vs_velocity.png : stagnation heat flux vs entry velocity (fixed rho, Rn)
- qdot_vs_density.png  : stagnation heat flux vs density (fixed v, Rn)

Usage:
    python -m src.plot_profiles
"""

import os
from typing import List

import matplotlib.pyplot as plt  # dev dependency (matplotlib)

from .models import ReentryCase, sutton_graves_heat_flux


def ensure_outdir(path: str = "figures") -> str:
    os.makedirs(path, exist_ok=True)
    return path


def linspace(start: float, stop: float, num: int) -> List[float]:
    """Tiny numpy.linspace replacement to avoid extra deps."""
    if num <= 1:
        return [start]
    step = (stop - start) / (num - 1)
    return [start + i * step for i in range(num)]


def plot_qdot_vs_velocity(
    rho_kgm3: float = 0.02,
    Rn_m: float = 0.5,
    v_min: float = 6500.0,
    v_max: float = 8000.0,
    n: int = 20,
    outdir: str = "figures",
) -> str:
    """
    Plot stagnation heat flux vs entry velocity for a fixed density and nose radius.
    q_dot ∝ sqrt(rho/Rn) * v^3 → strong cubic dependence on v.
    """
    velocities = linspace(v_min, v_max, n)
    qdots = []
    for v in velocities:
        case = ReentryCase(v_mps=v, rho=rho_kgm3, Rn=Rn_m)
        qdots.append(sutton_graves_heat_flux(case))

    plt.figure()
    plt.plot(velocities, qdots, linewidth=2.0)
    plt.xlabel("Entry velocity, m/s")
    plt.ylabel("Stagnation heat flux, W/m²")
    plt.title("Sutton–Graves q̇ vs Velocity (ρ, Rn fixed)")
    plt.grid(True, linestyle="--", alpha=0.4)

    ensure_outdir(outdir)
    out_path = os.path.join(outdir, "qdot_vs_velocity.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()
    return out_path


def plot_qdot_vs_density(
    v_mps: float = 7500.0,
    Rn_m: float = 0.5,
    rho_min: float = 0.005,
    rho_max: float = 0.05,
    n: int = 20,
    outdir: str = "figures",
) -> str:
    """
    Plot stagnation heat flux vs density for a fixed entry velocity and nose radius.
    q_dot ∝ sqrt(rho/Rn) → square-root dependence on density.
    """
    densities = linspace(rho_min, rho_max, n)
    qdots = []
    for rho in densities:
        case = ReentryCase(v_mps=v_mps, rho=rho, Rn=Rn_m)
        qdots.append(sutton_graves_heat_flux(case))

    plt.figure()
    plt.plot(densities, qdots, linewidth=2.0)
    plt.xlabel("Freestream density, kg/m³")
    plt.ylabel("Stagnation heat flux, W/m²")
    plt.title("Sutton–Graves q̇ vs Density (v, Rn fixed)")
    plt.grid(True, linestyle="--", alpha=0.4)

    ensure_outdir(outdir)
    out_path = os.path.join(outdir, "qdot_vs_density.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()
    return out_path


def main() -> None:
    p1 = plot_qdot_vs_velocity()
    p2 = plot_qdot_vs_density()
    print("Saved figures:")
    print(" -", p1)
    print(" -", p2)


if __name__ == "__main__":
    main()
