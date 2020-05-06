from enum import Enum
import os,sys,inspect

current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import table

class RoofCondition(Enum):
    RoofCondition1 = 1  # برف ریز
    RoofCondition2 = 2  # نیمه برف گیر
    RoofCondition3 = 3  # برف گیرi


class RoofSurfType(Enum):
    RoofSurfType1 = 1
    RoofSurfType2 = 2


class EnvCondition(Enum):
    EnvCondition1 = 1
    EnvCondition2 = 2
    EnvCondition3 = 3


class TempCondition(Enum):
    TempCondition1 = 1
    TempCondition2 = 2
    TempCondition3 = 3
    TempCondition4 = 4


class RoofType(Enum):
    RoofType1 = 1
    RoofType2 = 2
    RoofType3 = 3


def Ce(roof_condition: RoofCondition, env_condition: EnvCondition) -> float:
    rCe = 0
    if roof_condition == RoofCondition.RoofCondition1:
        if env_condition == EnvCondition.EnvCondition1:
            rCe = 0.9
        elif env_condition == EnvCondition.EnvCondition2:
            rCe = 0.9
        elif env_condition == EnvCondition.EnvCondition3:
            rCe = 0.8
    elif roof_condition == RoofCondition.RoofCondition2:
        if env_condition == EnvCondition.EnvCondition1:
            rCe = 1
        elif env_condition == EnvCondition.EnvCondition2:
            rCe = 1
        elif env_condition == EnvCondition.EnvCondition3:
            rCe = 0.9
    elif roof_condition == RoofCondition.RoofCondition3:
        if env_condition == EnvCondition.EnvCondition1:
            rCe = 1.2
        elif env_condition == EnvCondition.EnvCondition2:
            rCe = 1.1
        elif env_condition == EnvCondition.EnvCondition3:
            rCe = 1
    
    return rCe


def Ct(temp_condition: TempCondition) -> float:
    rCt = 0
    if temp_condition == TempCondition.TempCondition1:
        rCt = 1
    elif temp_condition == TempCondition.TempCondition2:
        rCt = 1.1
    elif temp_condition == TempCondition.TempCondition3:
        rCt = 1.2
    elif temp_condition == TempCondition.TempCondition4:
        rCt = 1.3

    return rCt

def alpha0(roof_surf_type: RoofSurfType, ct: float) -> float:
    ralpha0 = 0
    if roof_surf_type == RoofSurfType.RoofSurfType1:
        if ct == 1:
            ralpha0 = 5
        elif ct == 1.1:
            ralpha0 = 10
        elif ct > 1.1:
            ralpha0 = 15
    elif roof_surf_type == RoofSurfType.RoofSurfType2:
        if ct == 1:
            ralpha0 = 30
        elif ct > 1:
            ralpha0 = 45

    return ralpha0

def Cs(alpha: float, alpha0: float) -> float:
    rCs = 0
    if alpha <= alpha0:
        rCs = 1
    elif (alpha > alpha0) and (alpha < 70):
        rCs = 1 - ((alpha - alpha0)/(70 - alpha0))
    elif alpha >= 70:
        rCs = 0

    return rCs


def I(structure_group: float) -> float:
    return table.getdata(table.Tables.ImportanceCOE, 
            table.ImpCOEFields.Group, structure_group)[table.ImpCOEFields.Snow]

print(I(1))
