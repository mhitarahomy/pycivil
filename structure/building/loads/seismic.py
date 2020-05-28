'''Determine seismic forces for building
   source is 2800(4th)'''

import table
import math
from enum import Enum


class AreaCondition(Enum):
    '''Area condition
        A=0.2 & A=0.25 -> LowRisk
        A=0.3 & A=0.35 -> HighRisk'''
    HighRisk = 0
    LowRisk = 1


class SoilGroup(Enum):
    Group1 = 1
    Group2 = 2
    Group3 = 3
    Group4 = 4


def Is(group: int) -> float:
    '''Calculate importance coefficient for seismic load
        group -> group of structure based on 2800(4th) P.5 part 6-1'''
    return table.getdata(
            table.Tables.ImportanceCOE,
            table.ImpCOEFields.Group, group)[table.ImpCOEFields.Seismic]


def A(zone: int) -> float:
    '''Calculate A
        zone -> based on seismic hazard zonation map of iran'''
    return table.getdata(
            table.Tables.Acceleration,
            table.AccelFields.ZONE, zone)[table.AccelFields.A]


def Ru(strucsystem: str, seismicsystem: str):
    '''Calculate behaviour coefficient of structure
        strucsystem, seismicsystem -> based on 2800(4th) p.34 table 4-3'''
    return table.getdata(
            table.Tables.BehaviorCOE,
            table.BehCOEFields.StructureSystem, strucsystem,
            table.BehCOEFields.SeismicSystem,
            seismicsystem)[table.BehCOEFields.Ru]


class Soil:
   def __init__(self, soilgroup: SoilGroup, areacondition: AreaCondition):
       '''Calculate soil factors
          soilgroup -> soil group based on 2800 (4th) P.19 table 3-2
          areacondition -> area condition based on A'''
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
                             table.BehCOEFields.StructureSystem, strsystem)
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


def T(ta: float, tm: float) -> float:
    return min(1.25 * ta, tm)


def B1(t: float, soil: Soil) -> float:
    rB1 = 0
    if t > 0 and t < soil.T0:
        rB1 = soil.S0 + (soil.S - soil.S0 + 1) * (t / soil.T0)
    elif soil.T0 < T and T < soil.Ts:
        rB1 = soil.S + 1
    elif t > soil.Ts:
        rB1 = (soil.S + 1) * (soil.Ts / T)

    return rB1


def N(t: float, soil: Soil, areacondition: AreaCondition) -> float:
    rN = 0
    if areacondition == AreaCondition.HighRisk:
        if t < soil.Ts:
            rN = 1
        elif soil.Ts < t and t < 4:
            rN = ((0.7 / (4 - soil.Ts)) * (t - soil.Ts)) + 1
        elif t > 4:
            rN = 1.7
    elif areacondition == AreaCondition.LowRisk:
        if t < soil.Ts:
            rN = 1
        elif soil.Ts < t and t < 4:
            rN = ((0.4 / (4 - soil.Ts)) * (t - soil.Ts)) + 1
        elif t > 4:
            rN = 1.4

    return rN


def B(b1: float, n: float) -> float:
    return b1 * n


def C(a: float, b: float, i:float, ru:float) -> float:
    return (a * b * i) / ru


def MinBaseShear(a: float, i: float, w: float) -> float:
    return 0.12 * a * i * w


def BaseShear(c: float, w: float) -> float:
    return c * w


def StaticBaseShear(minbs: float, bs: float) -> float:
    return min(minbs, bs)


strucsys = table.getlist(table.Tables.BehaviorCOE,
                         table.BehCOEFields.StructureSystem)[2]

seismicsys = table.getlist(table.Tables.BehaviorCOE,
                           table.BehCOEFields.SeismicSystem,
                           table.BehCOEFields.StructureSystem, strucsys)[0]
print(Ta(strucsys, seismicsys, 50))
