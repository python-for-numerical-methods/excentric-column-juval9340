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

    # הגדרת עומס קריסה של אוילר (החסם העליון)
    euler_load = (math.pi**2 * E * (A * r**2)) / (L**2)

    def f(P):
        # חישוב המאמץ המקסימלי לפי נוסחת הסקנט
        argument = (L / (2.0 * r)) * math.sqrt(P / (E * A))
        
        # הגנה מפני חלוקה באפס או ערכים קרובים מדי לאסימפטוטה
        cos_val = math.cos(argument)
        if cos_val <= 1e-10:
            return float('inf') 
            
        sigma_max = (P / A) * (1.0 + (e * c / r**2) * (1.0 / cos_val))
        return sigma_max - sigma_allow

    # הגדרת גבולות לשיטת החצייה (הורדנו ל-0.95 כדי למנוע קריסת קוסינוס)
    P_low = 1e-6
    P_high = 0.95 * euler_load

    tol = 1e-6
    max_iter = 1000

    # נוודא שהפונקציה אכן משנה סימן בין הגבולות
    f_low = f(P_low)
    f_high = f(P_high)
    
    # אם אין שינוי סימן, נחזיר את הגבול העליון כברירת מחדל בטוחה
    if f_low * f_high > 0:
        return float(P_high)

    # לולאת חצייה
    for _ in range(max_iter):
        P_mid = (P_low + P_high) / 2.0
        f_mid = f(P_mid)

        if abs(f_mid) < tol or (P_high - P_low) < tol:
            return float(P_mid)

        if f(P_low) * f_mid < 0:
            P_high = P_mid
        else:
            P_low = P_mid
            f_low = f_mid

    return float((P_low + P_high) / 2.0)
