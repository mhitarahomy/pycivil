import json

class Tables:
    Acceleration = "ACCELERATION.json"

class AccelFields:
    A = "A"
    DESCRIPTION = "DESCRIPTION"
    ZONE = "ZONE"

def getdata(tablename: str, *condition):
    try:
        with open(tablename) as jsonfile:
            jsondata = json.load(jsonfile)
            if  condition == ():
                return jsondata
            rdata = None
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

def getlist(tablename: str, field: str):
    try:
        with open(tablename) as jsonfile:
            jsondata = json.load(jsonfile)
            rdata = []
            for data in jsondata:
                if not (data[field] in rdata):
                    rdata.append(data[field])
    except IOError:
        print("File not accessible")
    except:
        print("File Error")

    return rdata


print(getlist(Tables.Acceleration, AccelFields.A))
