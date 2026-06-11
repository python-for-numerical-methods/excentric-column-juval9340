def find_critical_load(L, E, A, r, c, e, sigma_allow):
    """
    L: אורך במ"מ
    E: מודול אלסטיות ב-MPa
    A: שטח חתך בממ"ר
    r: רדיוס אינרציה במ"מ
    c: מרחק לסיב קיצוני במ"מ
    e: אקסצנטריות במ"מ
    sigma_allow: מאמץ מותר ב-MPa

    Return: העומס P בניוטון (float)
    """
    # כתבו כאן את הקוד
import numpy as np
from scipy.optimize import bisect

def f(P):
    sigma_max = (P / A) * (
        1 + (e * c / r**2) *
        (1 / np.cos((L / (2 * r)) * np.sqrt(P / (E * A))))
    )
    return sigma_max - sigma_allow

euler_load = (np.pi**2 * E * (A * r**2)) / (L**2)

P = bisect(f, 1e-6, 0.999 * euler_load)

return float(P)
