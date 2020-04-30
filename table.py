import json
import os

currpath = os.path.dirname(os.path.abspath(__file__))

class Tables:
    """This class is for table names"""
    Acceleration = currpath + "/tables/ACCELERATION.json"
    BehaviorCOE = currpath + "/tables/BEHAVIOR_COEFFICIENT.json"
    ImportanceCOE = currpath + "/tables/IMPORTANCE_COEFFICIENT.json"
    LiveLoads = currpath + "/tables/LIVE_LOADS.json"
    Materials = currpath + "/tables/MATERIALS.json"
    SnowLoadZone = currpath + "/tables/SNOW_LOAD_ZONE.json"
    SoilLoad = currpath + "/tables/SOIL_LOAD.json"
    SoilTypeSeismic = currpath + "/tables/SOIL_TYPES_SEISMIC.json"
    StructureGroup = currpath + "tables/STRUCTURE_GROUP.json"

class AccelFields:
    """Acceleration table fields"""
    A = "A"
    DESCRIPTION = "DESCRIPTION"
    ZONE = "ZONE"

class BehCOEFields:
    """Behavior Coefficient table fields"""
    StructureSystem = "STRUCTURE_SYSTEM"
    SeismicSystem = "SEISMIC_SYSTEM"
    Ru = "Ru"
    Omega0 = "Omega0"
    Hm = "Hm"
    Cd = "Cd"

class ImpCOEFields:
    """Importance Coefficient table fields"""
    Group = "GROUP_NUM"
    Ice = "ICE"
    Seismic = "SEISMIC"
    Snow = "SNOW"
    Wind = "WIND"

class LiveLoadFields:
    """Live loads table fields"""
    Category = "CATEGORY"
    Description = "DESCRIPTION"
    ConcentratedLoad = "CENCENTRATED_LOAD"
    UniformLoad = "UNIFORM_LOAD"
    Comment = "COMMENT"

class MaterialFields:
    """Material table fields"""
    ID = "ID"
    MaterialType = "MATERIAL_TYPE"
    Description = "DESCRIPTION"
    Density = "DENSITY"

class SnowLoadZoneFields:
    """Snow load zone table fields"""
    Zone = "ZONE_ID"
    Description = "DESCRIPTION"
    Magnitude = "LOAD_MAGNITUDE"

class SoilLoadFields:
    """Soil load table fields"""
    Description = "DESCRIPTION"
    Group = "SOIL_GROUP"
    Magnitude = "LOAD_MAGNITUDE"
    Comment = "COMMENT"

class SoilTypeSeiemicFields:
    """Soil type seismic table fields"""
    Type = "SOIL_TYPE"
    Description = "DESCRIPTION"
    S0H = "S0H"
    S0L = "S0L"
    SH = "SH"
    SL = "SL"
    T0 = "T0"
    Ts = "Ts"
    vsH = "vsH"
    vsL = "vsL"
    NL = "NL"
    CuL = "CuL"

class StrucGroupFields:
    """Structure group table fields"""
    Group = "GROUP_ID"
    Description = "DESCRIPTION"

def getdata(tablename: str, *condition):
    """Get data from Tables class
    condition is list with length of 2 or 4""" 
    rdata = None
    try:
        with open(tablename) as jsonfile:
            jsondata = json.load(jsonfile)
            if  condition == ():
                return jsondata
            for data in jsondata:
                if len(condition) == 2:
                    if data[condition[0]] == condition[1]:
                        rdata = data;
                elif len(condition) == 4:
                    if data[condition[0]] == condition[1] and data[condition[2]] == condition[3]:
                        rdata = data
    except IOError:
        print("File not accessible")
    except:
        print("File Error")
    
    return rdata

def getlist(tablename: str, field: str, *condition):
    """Get list of data from Table class
    condition is list with length of 2"""
    rdata = []
    try:
        with open(tablename) as jsonfile:
            jsondata = json.load(jsonfile)
            if condition == ():
                for data in jsondata:
                    if not (data[field] in rdata):
                        rdata.append(data[field])
            elif len(condition) == 2:
                for data in jsondata:
                    if (not (data[field] in rdata)) and data[condition[0]] == condition[1]:
                        rdata.append(data[field])
    except IOError:
        print("File not accessible")
    except:
        print("File Error")

    return rdata


print(getdata(Tables.ImportanceCOE, ImpCOEFields.Group, 2))
print(getlist(Tables.ImportanceCOE, ImpCOEFields.Group))
