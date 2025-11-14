from src.atmosphere import rho_exponential

def test_density_decreases_with_altitude():
    assert rho_exponential(0.0) > rho_exponential(10000.0)
