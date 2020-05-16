'''functions for bridge loads '''


def CoincidenceCoefficient(numoflanes: int) -> float:
    '''numoflanes -> number of traffic lanes
       return -> coincidence coefficient (coefficient)'''

    rcoincoef = 0
    if numoflanes == 1 or numoflanes == 2:
        rcoincoef = 1
    elif numoflanes == 3:
        rcoincoef = 0.9
    elif numoflanes > 3:
        rcoincoef = 0.75

    return rcoincoef


def ImpactCoefficient(h: float, l1: float, l2: float = 0) -> float:
    ''' h -> height of embankment (meter)
        l1, l2 -> span (meter)
        return -> impact coefficient (coefficient)'''

    rimpcoef = 0
    if l2 != 0:
        if h>2 or min(l1, l2) >= 60:
            rimpcoef = 1
        else:
            rimpcoef = 1.3 - 0.005 * min(l1, l2) - 0.15 * h
    else:
        if h>2 or l1 >=60:
            rimpcoef = 1
        else:
            rimpcoef = 1.3 - 0.005 * l1 - 0.15 * h

    return rimpcoef


def BrakeLoad(l0: float) -> float:
    '''l0 -> distance of expansion seams (meter)
       return -> brake load (ton)'''

    return min(200 + 7 * l0, 400) / 10


def EccentricityLoad(r: float, v: float, w:float = 40) -> float:
    '''r -> radius of arc (meter)
       v -> vehicle design speed (meter / second)
       w -> vehicle weight (ton)
       return -> eccentricity load (ton)'''
    g = 9.81
    kc = (v * v) / (r * g)
    return kc * w


#print(EccentricityLoad(500, 20))

