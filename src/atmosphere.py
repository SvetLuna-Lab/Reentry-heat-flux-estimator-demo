import math

def rho_exponential(h_m: float, rho0: float = 1.225, H_m: float = 7500.0) -> float:
    """Exponential density model ρ = ρ0 * exp(-h/H)."""
    return rho0 * math.exp(-max(h_m, 0.0) / max(H_m, 1.0))
