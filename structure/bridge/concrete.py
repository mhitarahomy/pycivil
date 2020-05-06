import math


def Ec(fc):
    return 1580 * math.sqrt(fc)

def fr(fc):
    return 2 * math.sqrt(fc)

def beta1(fc):
    if fc < 280 :
        return 0.85
    else:
        return 0.85-((0.05*(fc-280))/70)

def rhob(fc, fy):
    return 0.85 * beta1(fc) * (fc/fy) * (600/(600+fy))

def rhomax(fc, fy):
    return 0.75 * rhob(fc, fy)

