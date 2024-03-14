import pytest

from ..optn.vol import IV


def test_newton_vol():
    S = 3977.0
    K = 4050.0
    r = 0.0
    t = 0.00
    T = 1.25 / 365.0

    iv = IV(S, K, r, t, T)
    price = 29.82
    assert iv.newton_vol(price) == pytest.approx(0.633, rel=1e-1)
    # assert iv.newton_vol(price, sigma_est=0.1) == pytest.approx(0.2)
