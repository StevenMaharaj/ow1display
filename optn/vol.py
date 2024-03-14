from dataclasses import dataclass

from . import bs


@dataclass
class IV:
    S: float
    K: float
    r: float
    t: float
    T: float

    def newton_vol(self, option_price: float, sigma_est=2.0, tol=0.0001, max_iter=100):
        sigma = sigma_est
        for _ in range(max_iter):
            price = bs.BSM_call_value(self.S, self.K, self.t, self.T, self.r, sigma)
            vega = bs.BSM_vega(self.S, self.K, self.t, self.T, self.r, sigma)
            diff = option_price - price
            if abs(diff) < tol:
                return sigma
            try:
                sigma = sigma + diff / vega
            except ZeroDivisionError:
                print("ZeroDivisionError")
                print("option_price:", option_price)
                print("price:", price)
                print("vega:", vega)
                return 0

        return sigma
