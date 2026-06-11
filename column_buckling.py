import numpy as np
from scipy import optimize

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
    def column_stress_error(P_val, L_val, E_val, A_val, r_val, c_val, e_val, sigma_allow_val):
        sigma_max = (P_val / A_val) * (
            1 + (e_val * c_val / r_val**2) * (1 / np.cos((L_val / (2 * r_val)) * np.sqrt(P_val / (E_val * A_val))))
        )
        return sigma_max - sigma_allow_val

    P_critical = optimize.newton(
        lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow), 
        500000
    )

    return float(P_critical)
