'''Determine seismic forces for building
   source is 2800(5th)'''

import table
from enum import Enum


class AreaCondition(Enum):
    HighRisk = 0
    LowRisk = 1


class SoilGroup(Enum):
    Group1 = 1
    Group2 = 2
    Group3 = 3
    Group4 = 4


def Is(group: int) -> float:
    return table.getdata(
            table.Tables.ImportanceCOE,
            table.ImpCOEFields.Group, group)[table.ImpCOEFields.Seismic]


def A(zone: int) -> float:
    return table.getdata(
            table.Tables.Acceleration,
            table.AccelFields.ZONE, zone)[table.AccelFields.A]


def Ru(strucsystem: str, seismicsystem: str):
    return table.getdata(
            table.Tables.BehaviorCOE,
            table.BehCOEFields.StructureSystem, strucsystem,
            table.BehCOEFields.SeismicSystem,
            seismicsystem)[table.BehCOEFields.Ru]


class Soil:

    def __init__(self, soilgroup: SoilGroup, areacondition: AreaCondition):
        soil = table.getdata(
                table.Tables.SoilTypeSeismic,
                table.SoilTypeSeiemicFields.Type,
                soilgroup.value)
        self.T0 = soil[table.SoilTypeSeiemicFields.T0]
        self.Ts = soil[table.SoilTypeSeiemicFields.Ts]
        if areacondition == AreaCondition.LowRisk:
            self.S = soil[table.SoilTypeSeiemicFields.SL]
            self.S0 = soil[table.SoilTypeSeiemicFields.S0L]
        elif areacondition == AreaCondition.HighRisk:
            self.S = soil[table.SoilTypeSeiemicFields.SH]
            self.S0 = soil[table.SoilTypeSeiemicFields.S0H]


soil = Soil(SoilGroup.Group3, AreaCondition.HighRisk)
print(soil.S0)
