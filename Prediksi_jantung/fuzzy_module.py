def fuzzy_risk_level(chol, bp, hr):
    if chol > 240 and bp > 140:
        return "Tinggi"
    elif chol > 200 or bp > 130:
        return "Sedang"
    else:
        return "Rendah"
