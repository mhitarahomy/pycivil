import math
from structure.bridge.loads.load import ImpactCoefficient


def DeckDeadLoad(S: float, effS: float, decklayers: list[float, float]):
    dload: float = 0
    for x, y in decklayers:
        ddload = dload + (x * y)
    return (dload * math.pow(effS, 2)) / 10, (dload * S) / 2


def DeckLiveLoad(P: float, effS: float):
    effS_ft = effS * 3.28084
    P_imp = P * 2204.62
    Mll_imp = (P_imp * (effS_ft + 2)) / 32
    Mll = Mll_imp / 2204.62
    return Mll * ImpactCoefficient(0, effS) * 0.8, Mll * ImpactCoefficient(0, effS) * 0.8 * (5 / effS)


print(DeckLiveLoad(8, 1.25))
