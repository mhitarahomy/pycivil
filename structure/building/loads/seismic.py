'''Determine seismic forces for building
   source is 2800(5th)'''

import table
import math
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


def Ta(strucsystem: str, seismicsystem: str, h: float, 
       isolator: bool = False) -> float:
    rta = 0
    struclist = table.getlist(
            table.Tables.BehaviorCOE, table.BehCOEFields.StructureSystem)
    def seismiclist(strsystem: str) -> str:
        return table.getlist(
                             table.Tables.BehaviorCOE, 
                             table.BehCOEFields.SeismicSystem,
                             table.BehCOEFields.StructureSystem,strsystem)
    if strucsystem == struclist[2] and \
       seismicsystem == seismiclist(struclist[2])[0] or \
       seismicsystem == seismiclist(struclist[2])[1] or \
       seismicsystem == seismiclist(struclist[2])[2]:
           if isolator:
               rta = 0.8 * 0.05 * math.pow(h, 0.9)
           else: 
               rta = 0.05 * math.pow(h, 0.9)
    elif strucsystem == struclist[2] and \
       seismicsystem == seismiclist(struclist[2])[3] or \
       seismicsystem == seismiclist(struclist[2])[4] or \
       seismicsystem == seismiclist(struclist[2])[5]:
           if isolator:
               rta = 0.8 * 0.08 * math.pow(h, 0.75)
           else: 
               rta = 0.08 * math.pow(h, 0.75)
    elif strucsystem == struclist[1] and \
         seismicsystem == seismiclist(struclist[1])[4]:
           rta = 0.08 * math.pow(h, 0.75)
    else:
        rta = 0.05 * math.pow(h, 0.75)

    return rta


strucsys = table.getlist(table.Tables.BehaviorCOE, 
        table.BehCOEFields.StructureSystem)[2]

seismicsys = table.getlist(table.Tables.BehaviorCOE, 
                        table.BehCOEFields.SeismicSystem,
                        table.BehCOEFields.StructureSystem,strucsys)[0]
print(Ta(strucsys, seismicsys, 50))
