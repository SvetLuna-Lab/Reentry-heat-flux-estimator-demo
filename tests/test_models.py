from src.models import ReentryCase, sutton_graves_heat_flux, ballistic_coefficient, peak_g_load_estimate

def test_heat_flux_scales_with_v3():
    c1 = ReentryCase(v_mps=7000.0, rho=0.02, Rn=0.5)
    c2 = ReentryCase(v_mps=8000.0, rho=0.02, Rn=0.5)
    q1 = sutton_graves_heat_flux(c1)
    q2 = sutton_graves_heat_flux(c2)
    assert q2 > q1 and q2/q1 > 1.2

def test_ballistic_coefficient_units():
    c = ReentryCase(v_mps=7500.0, rho=0.02, Rn=0.5, mass=1500.0, Cd=1.5, area=2.0)
    beta = ballistic_coefficient(c)
    assert 400.0 < beta < 1200.0

def test_peak_g_order_of_magnitude():
    gpk = peak_g_load_estimate(7800.0)
    assert 2.0 < gpk < 10.0
