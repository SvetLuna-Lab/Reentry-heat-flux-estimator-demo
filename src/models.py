import math
from dataclasses import dataclass

@dataclass
class ReentryCase:
    v_mps: float      # entry speed [m/s]
    rho: float        # freestream density [kg/m^3]
    Rn: float         # nose radius [m]
    k: float = 1.83e-4  # Sutton–Graves constant for Earth (approx, SI)
    mass: float = 1000.0
    Cd: float = 1.2
    area: float = 1.0

def sutton_graves_heat_flux(case: ReentryCase) -> float:
    """
    Convective stagnation-point heat flux (W/m^2), Sutton–Graves form:
    q_dot = k * sqrt(rho / Rn) * v^3
    Uses SI units. k may vary by atmosphere/gas; this is an approximate Earth value.
    """
    return case.k * math.sqrt(case.rho / max(case.Rn, 1e-6)) * (case.v_mps ** 3)

def ballistic_coefficient(case: ReentryCase) -> float:
    """
    Ballistic coefficient beta = m / (Cd * A) [kg/m^2]
    Higher beta → deeper penetration, higher heating.
    """
    return case.mass / (max(case.Cd * case.area, 1e-9))

def peak_g_load_estimate(v_entry: float, scale_height: float = 7500.0) -> float:
    """
    Very rough g-load estimate using deceleration over a scale height H:
    a ~ v^2 / (2H). Return in g0 units.
    """
    g0 = 9.80665
    a = (v_entry ** 2) / (2.0 * max(scale_height, 1.0))
    return a / g0
