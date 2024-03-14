import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.family"] = "serif"
from scipy.integrate import quad


def dN(x):
    return math.exp(-0.5 * x**2) / math.sqrt(2 * math.pi)


def N(d):
    return quad(lambda x: dN(x), -20, d, limit=50)[0]


def d1f(St, K, t, T, r, sigma):
    d1 = (math.log(St / K) + (r + 0.5 * sigma**2) * (T - t)) / (
        sigma * math.sqrt(T - t)
    )
    return d1


def BSM_call_value(
    St: float, K: float, t: float, T: float, r: float, sigma: float
) -> float:
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * N(d1) - math.exp(-r * (T - t)) * K * N(d2)
    return call_value


def BSM_put_value(
    St: float, K: float, t: float, T: float, r: float, sigma: float
) -> float:
    put_value = BSM_call_value(St, K, t, T, r, sigma) - St + math.exp(-r * (T - t)) * K
    return put_value


def plot_values(function):
    # Plots European option values for different parameters c.p. '''
    plt.figure(figsize=(10, 8.3))
    points = 100
    #
    # Model Parameters
    #
    St = 100.0  # index level
    K = 100.0  # option strike
    t = 0.0  # valuation date
    T = 1.0  # maturity date
    r = 0.05  # risk-less short rate
    sigma = 0.2  # volatility
    # C(K) plot
    plt.subplot(221)
    klist = np.linspace(80, 120, points)
    vlist = [function(St, K, t, T, r, sigma) for K in klist]
    plt.plot(klist, vlist)
    plt.grid()
    plt.xlabel("strike $K$")
    plt.ylabel("present value")
    # C(T) plot
    plt.subplot(222)
    tlist = np.linspace(0.0001, 1, points)
    vlist = [function(St, K, t, T, r, sigma) for T in tlist]
    plt.plot(tlist, vlist)
    plt.grid(True)
    plt.xlabel("maturity $T$")
    # C(r) plot
    plt.subplot(223)
    rlist = np.linspace(0, 0.1, points)
    vlist = [function(St, K, t, T, r, sigma) for r in rlist]
    plt.plot(tlist, vlist)
    plt.grid(True)
    plt.xlabel("short rate $r$")
    plt.ylabel("present value")
    plt.axis("tight")
    # C(sigma) plot
    plt.subplot(224)
    slist = np.linspace(0.01, 0.5, points)
    vlist = [function(St, K, t, T, r, sigma) for sigma in slist]
    plt.plot(slist, vlist)
    plt.grid(True)
    plt.xlabel("volatility $\\sigma$")
    plt.tight_layout()
    plt.show()


def BSM_call_delta(
    St: float, K: float, t: float, T: float, r: float, sigma: float
) -> float:
    d1 = d1f(St, K, t, T, r, sigma)
    delta = N(d1)
    return delta


def BSM_put_delta(
    St: float, K: float, t: float, T: float, r: float, sigma: float
) -> float:
    delta = BSM_call_delta(St, K, t, T, r, sigma) - 1.0
    return delta


def BSM_gamma(St: float, K: float, t: float, T: float, r: float, sigma: float) -> float:
    d1 = d1f(St, K, t, T, r, sigma)
    gamma = dN(d1) / (St * sigma * math.sqrt(T - t))
    return gamma


def BSM_vega(St: float, K: float, t: float, T: float, r: float, sigma: float) -> float:
    d1 = d1f(St, K, t, T, r, sigma)
    vega = St * dN(d1) * math.sqrt(T - t)
    return vega


def BSM_call_theta(St, K, t, T, r, sigma):
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    theta = -(
        St * dN(d1) * sigma / (2 * math.sqrt(T - t))
        + r * K * math.exp(-r * (T - t)) * N(d2)
    )
    return theta


def BSM_put_theta(
    St: float, K: float, t: float, T: float, r: float, sigma: float
) -> float:
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    theta = -(
        St * dN(d1) * sigma / (2 * math.sqrt(T - t))
        - r * K * math.exp(-r * (T - t)) * N(-d2)
    )
    return theta


def BSM_call_rho(
    St: float, K: float, t: float, T: float, r: float, sigma: float
) -> float:
    d2 = d1f(St, K, t, T, r, sigma) - sigma * math.sqrt(T - t)
    rho = K * (T - t) * math.exp(-r * (T - t)) * N(d2)
    return rho


def BSM_put_rho(
    St: float, K: float, t: float, T: float, r: float, sigma: float
) -> float:
    d2 = d1f(St, K, t, T, r, sigma) - sigma * math.sqrt(T - t)
    rho = -K * (T - t) * math.exp(-r * (T - t)) * N(-d2)
    return rho
