import pytest

from .. import bs
from ..vol import IV


def test_delta():
    S = 3977.0
    K = 4050.0
    r = 0.0
    t = 0.00
    T = 1.25 / 365.0

    iv = IV(S, K, r, t, T)
    price = 29.82
    sigma = iv.newton_vol(price)
    assert bs.BSM_call_delta(S, K, t, T, r, sigma) == pytest.approx(0.32, rel=1e-2)

    # assert iv.newton_vol(price, sigma_est=0.1) == pytest.approx(0.2)


def test_gamma():
    S = 3977.0
    K = 4050.0
    r = 0.0
    t = 0.00
    T = 1.25 / 365.0

    iv = IV(S, K, r, t, T)
    price = 29.82
    sigma = iv.newton_vol(price)
    assert bs.BSM_gamma(S, K, t, T, r, sigma) == pytest.approx(0.00236, rel=1e-1)


def test_vega():
    S = 3977.0
    K = 4050.0
    r = 0.0
    t = 0.00
    T = 1.25 / 365.0

    iv = IV(S, K, r, t, T)
    price = 29.82
    sigma = iv.newton_vol(price)
    assert bs.BSM_vega(S, K, t, T, r, sigma) * 0.01 == pytest.approx(0.84, rel=1e-1)
