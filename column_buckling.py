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
import math
    def f(P):
        # חישוב המאמץ המקסימלי לפי נוסחת הסקנט
        sigma_max = (P / A) * (
            1.0 + (e * c / r**2) *
            (1.0 / math.cos((L / (2.0 * r)) * math.sqrt(P / (E * A))))
        )
        return sigma_max - sigma_allow

    # חישוב עומס קריסה של אוילר (החסם העליון)
    euler_load = (math.pi**2 * E * (A * r**2)) / (L**2)

    # הגדרת גבולות לשיטת החצייה
    P_low = 1e-6
    P_high = 0.999 * euler_load

    # לולאת חצייה ידנית
    tol = 1e-6
    max_iter = 1000

    for _ in range(max_iter):
        P_mid = (P_low + P_high) / 2.0
        f_mid = f(P_mid)

        if abs(f_mid) < tol or (P_high - P_low) < tol:
            return float(P_mid)

        if f(P_low) * f_mid < 0:
            P_high = P_mid
        else:
            P_low = P_mid

    return float((P_low + P_high) / 2.0)
