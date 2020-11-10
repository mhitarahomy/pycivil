"""functions for concrete LFD design"""

import math

phis = 0.85
phif = 0.9
phia_tie = 0.7
phia_spiral = 0.75
phib = 0.7

ec = 0.003


def fr(fc: float) -> float:
    """fc -> extreme fiber compressive stress in concrete (kg/cm2)
       return -> modulus of rupture of concrete (kg/cm2)"""
    return 2 * math.sqrt(fc)


def beta1(fc: float) -> float:
    """fc -> extreme fiber compressive stress in concrete (kg/cm2)
       return -> ratio of depth of equivalent compression zone
                 to depth from fiber of maximum compressive strain to the neutral axis (coefficient)"""
    if fc < 280:
        rbeta1 = 0.85
    else:
        rbeta1 = 0.85 - ((0.05 * (fc - 280))/70)
    return rbeta1


def rhob(fc: float, fy: float) -> float:
    """fc -> extreme fiber compressive stress in concrete (kg/cm2)
       fy -> specified yield strength of reinforcement (kg/cm2)
       return -> reinforcement ratio producing balanced strain conditions (coefficient)"""
    return 0.85 * beta1(fc) * (fc / fy) * (6000 / (6000 + fy))


def rhomax(fc: float, fy: float) -> float:
    """fc -> extreme fiber compressive stress in concrete (kg/cm2)
       fy -> specified yield strength of reinforcement (kg/cm2)
       return -> reinforcement ratio for maximum condition based on code (coefficient)"""
    return 0.75 * 0.85 * beta1(fc) * (fc / fy) * (6000 / (6000 + fy))


def CalcAs(fc: float, fy: float, b: float, d: float, Mu: float):
    """fc -> extreme fiber compressive stress in concrete (kg/cm2)
       fy -> specified yield strength of reinforcement (kg/cm2)
       b -> width of compression face of member (centimeter)
       d -> distance from extreme compression fiber to centroid of tension reinforcemen (centimeter)
       Mu ->  factored moment at section (kg.cm)
       return -> area of tension reinforcement (cm2)"""
    Mn = Mu / phis
    As = ((0.85 * fc * b * d) / fy) * (1 - math.sqrt(1 - ((4 * Mn) / (1.7 * fc * b * math.pow(d, 2)))))
    return As


print(rhomax(200, 4000))
