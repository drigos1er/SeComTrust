import json
import random

from faker import Faker
from tinydb import TinyDB
import random
import fjson_upload
import numpy as np

rand_data = Faker()
rand_data.seed_instance(0)
from datetime import datetime

db = TinyDB('db.json', indent=4)
l_resm = db.table("lresm")

# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary


def create_lresm(nborg):

    i = 1
    lresm = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    TypeFlagList = [0, 1]
    Weighttype = [0.3, 0.7]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for _ in range(0, nborg):

        lresm["res{}".format(str(i).zfill(2))] = {}
        lresm["res{}".format(str(i).zfill(2))]['id'] = rand_data.bothify(text="p_%%")
        lresm["res{}".format(str(i).zfill(2))]['resource'] = str(np.random.choice( ResFlagList,p=Weightres))
        lresm["res{}".format(str(i).zfill(2))]['sensibility'] = int(np.random.choice(SensdomFlagList,p=Weightsens))
        lresm["res{}".format(str(i).zfill(2))]['quantity'] = rand_data.random_int(1, 20)
        lresm["res{}".format(str(i).zfill(2))]['available'] = rand_data.random_int(1, 20)
        lresm["res{}".format(str(i).zfill(2))]['state'] = int(np.random.choice(StateFlagList,p=Weight))
        lresm["res{}".format(str(i).zfill(2))]['secdom'] = int(np.random.choice( SecdomFlagList,p=Weightsec))
        lresm["res{}".format(str(i).zfill(2))]['typep'] = int(np.random.choice(TypeFlagList, p=Weighttype))
        i += 1

    lresmjson = json.dumps(lresm)

    with open("l_resm.json", "w") as outfile:
        json.dump(lresm, outfile, indent=4)

    return lresmjson




def create_ltram(nborg):
    i = 1
    ltram = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for _ in range(0, nborg):

        ltram["t{}".format(str(i).zfill(2))] = {}
        ltram["t{}".format(str(i).zfill(2))]['id'] = rand_data.bothify(text="p_%%")
        ltram["t{}".format(str(i).zfill(2))]['resource'] = str(np.random.choice( ResFlagList,p=Weightres))
        ltram["t{}".format(str(i).zfill(2))]['sensibility'] = int(np.random.choice(SensdomFlagList,p=Weightsens))
        ltram["t{}".format(str(i).zfill(2))]['quantity'] = rand_data.random_int(1, 20)
        ltram["t{}".format(str(i).zfill(2))]['tvalue'] = rand_data.random.random()
        ltram["t{}".format(str(i).zfill(2))]['specrep'] = rand_data.random.random()
        ltram["t{}".format(str(i).zfill(2))]['sla'] = int(np.random.choice( SecdomFlagList,p=Weightsec))
        ltram["t{}".format(str(i).zfill(2))]['bmode'] = rand_data.random_int(1, 4)
        ltram["t{}".format(str(i).zfill(2))]['result'] = 1
        ltram["t{}".format(str(i).zfill(2))]['tp_start'] = str(rand_data.date_time())
        ltram["t{}".format(str(i).zfill(2))]['tp_end'] = str(rand_data.date_time())
        i += 1

    ltramjson = json.dumps(ltram)

    with open("l_tram.json", "w") as outfile:
        json.dump(ltram, outfile, indent=4)


    print(ltramjson)


def create_lgtrans(ntrans):
    i = 1
    lgtrans = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.2, 0.8]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for _ in range(0, ntrans):

        lgtrans["t{}".format(str(i).zfill(2))] = {}
        lgtrans["t{}".format(str(i).zfill(2))]['idp'] = "p_68"
        lgtrans["t{}".format(str(i).zfill(2))]['idu'] = "p_29"
        lgtrans["t{}".format(str(i).zfill(2))]['resource'] = "rp_06"
        lgtrans["t{}".format(str(i).zfill(2))]['sensibility'] = 8
        lgtrans["t{}".format(str(i).zfill(2))]['quantity'] = rand_data.random_int(1, 20)
        lgtrans["t{}".format(str(i).zfill(2))]['tvaluep'] = rand_data.random.random()
        lgtrans["t{}".format(str(i).zfill(2))]['tvalueu'] = rand_data.random.random()
        lgtrans["t{}".format(str(i).zfill(2))]['specrep'] = rand_data.random.random()
        lgtrans["t{}".format(str(i).zfill(2))]['secdomp'] = int(np.random.choice( SecdomFlagList,p=Weightsec))
        lgtrans["t{}".format(str(i).zfill(2))]['secdomu'] = int(np.random.choice( SecdomFlagList,p=Weightsec))
        lgtrans["t{}".format(str(i).zfill(2))]['sla'] = int(np.random.choice( SecdomFlagList,p=Weightsec))
        lgtrans["t{}".format(str(i).zfill(2))]['bmode'] = rand_data.random_int(1, 4)
        lgtrans["t{}".format(str(i).zfill(2))]['result'] = int(np.random.choice( StateFlagList,p=Weight))
        lgtrans["t{}".format(str(i).zfill(2))]['tp_start'] = str(rand_data.date_time())
        lgtrans["t{}".format(str(i).zfill(2))]['tp_end'] = str(rand_data.date_time())
        i += 1

    lgtransjson = json.dumps(lgtrans)

    with open("l_gtrans.json", "w") as outfile:
        json.dump(lgtrans, outfile, indent=4)


    print(lgtransjson)

def create_lrepm(nborg):
    i = 1
    lrepm = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for _ in range(0, nborg):

        lrepm["rep{}".format(str(i).zfill(2))] = {}
        lrepm["rep{}".format(str(i).zfill(2))]['id'] = rand_data.bothify(text="p_%%")
        lrepm["rep{}".format(str(i).zfill(2))]['resource'] = str(np.random.choice( ResFlagList,p=Weightres))
        lrepm["rep{}".format(str(i).zfill(2))]['sensibility'] = int(np.random.choice(SensdomFlagList,p=Weightsens))
        lrepm["rep{}".format(str(i).zfill(2))]['specrep'] = rand_data.random.random()
        i += 1

    lrepmjson = json.dumps(lrepm)

    with open("l_repm.json", "w") as outfile:
        json.dump(lrepm, outfile, indent=4)
    print(lrepmjson)
    return lrepmjson


def create_lorgsd(nborg):
    i = 1
    lorgsd = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = ["L", "M" , "H"]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for _ in range(0, nborg):

        lorgsd["org{}".format(str(i).zfill(2))] = {}
        lorgsd["org{}".format(str(i).zfill(2))]['id'] = rand_data.bothify(text="p_%%")
        lorgsd["org{}".format(str(i).zfill(2))]['secdomp'] = str(np.random.choice(SecdomFlagList, p=Weightsec))
        lorgsd["org{}".format(str(i).zfill(2))]['globalrep'] = rand_data.random.random()
        lorgsd["org{}".format(str(i).zfill(2))]['assurlevel'] = rand_data.random.random()
        i += 1

    lorgsdjson = json.dumps(lorgsd)

    with open("l_orgsd.json", "w") as outfile:
        json.dump(lorgsd, outfile, indent=4)
    print(lorgsdjson)
    return lorgsdjson

def create_lsla(ntrans):
    i = 1
    lsla = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for _ in range(0, ntrans):

        lsla["sla{}".format(str(i).zfill(2))] = {}
        lsla["sla{}".format(str(i).zfill(2))]['idp'] = rand_data.bothify(text="p_%%")
        lsla["sla{}".format(str(i).zfill(2))]['idu'] = rand_data.bothify(text="p_%%")
        lsla["sla{}".format(str(i).zfill(2))]['resource'] = str(np.random.choice( ResFlagList,p=Weightres))
        lsla["sla{}".format(str(i).zfill(2))]['sensibility'] = int(np.random.choice(SensdomFlagList,p=Weightsens))
        lsla["sla{}".format(str(i).zfill(2))]['qtyu'] = rand_data.random_int(1, 20)
        lsla["sla{}".format(str(i).zfill(2))]['qtyp'] = rand_data.random_int(1, 20)
        lsla["sla{}".format(str(i).zfill(2))]['bmodeu'] = rand_data.random_int(1, 4)
        lsla["sla{}".format(str(i).zfill(2))]['bmodep'] = rand_data.random_int(1, 4)
        lsla["sla{}".format(str(i).zfill(2))]['tp_u'] = str(rand_data.date_time())
        lsla["sla{}".format(str(i).zfill(2))]['tp_p'] = str(rand_data.date_time())
        lsla["sla{}".format(str(i).zfill(2))]['tp_d'] = str(rand_data.date_time())
        lsla["sla{}".format(str(i).zfill(2))]['availlable_init'] = int(np.random.choice(SecdomFlagList, p=Weightsec))
        lsla["sla{}".format(str(i).zfill(2))]['availlable_p'] = int(np.random.choice(SecdomFlagList, p=Weightsec))
        lsla["sla{}".format(str(i).zfill(2))]['availlable_d'] = int(np.random.choice(SecdomFlagList, p=Weightsec))

        i += 1

    lslajson = json.dumps(lsla)

    with open("l_sla.json", "w") as outfile:
        json.dump(lsla, outfile, indent=4)


    print(lslajson)




def create_ltramperso(ltram,o_u,o_p,res,sens,qty,tvalue,specrep,sla,bmode,result,tp_start,tp_end):

    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}
    tl=len(ltram)

    i = tl + 1

    ltram["t{}".format(str(i).zfill(2))] = {}
    ltram["t{}".format(str(i).zfill(2))]['id'] = o_p
    ltram["t{}".format(str(i).zfill(2))]['resource'] = res
    ltram["t{}".format(str(i).zfill(2))]['sensibility'] = sens
    ltram["t{}".format(str(i).zfill(2))]['quantity'] = qty
    ltram["t{}".format(str(i).zfill(2))]['tvalue'] = tvalue
    ltram["t{}".format(str(i).zfill(2))]['specrep'] = specrep
    ltram["t{}".format(str(i).zfill(2))]['sla'] = sla
    ltram["t{}".format(str(i).zfill(2))]['bmode'] = bmode
    ltram["t{}".format(str(i).zfill(2))]['result'] = result
    ltram["t{}".format(str(i).zfill(2))]['tp_start'] = tp_start
    ltram["t{}".format(str(i).zfill(2))]['tp_end'] = tp_end


    with open("l_tram_"+o_u+".json", "w") as outfile:
          json.dump(ltram, outfile, indent=4)



def create_lgtransperso(lgtrans,o_u,o_p,res,sens,qty,tvaluep,tvalueu,specrep,secdomp,secdomu,sla,bmode,result,tp_start,tp_end):

    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}
    tl=len(lgtrans)

    i = tl + 1

    lgtrans["t{}".format(str(i).zfill(2))] = {}
    lgtrans["t{}".format(str(i).zfill(2))]['idp'] = o_p
    lgtrans["t{}".format(str(i).zfill(2))]['idu'] = o_u
    lgtrans["t{}".format(str(i).zfill(2))]['resource'] = res
    lgtrans["t{}".format(str(i).zfill(2))]['sensibility'] = sens
    lgtrans["t{}".format(str(i).zfill(2))]['quantity'] = qty
    lgtrans["t{}".format(str(i).zfill(2))]['tvaluep'] = tvaluep
    lgtrans["t{}".format(str(i).zfill(2))]['tvalueu'] = tvalueu
    lgtrans["t{}".format(str(i).zfill(2))]['specrep'] = specrep
    lgtrans["t{}".format(str(i).zfill(2))]['secdomp'] = secdomp
    lgtrans["t{}".format(str(i).zfill(2))]['secdomu'] = secdomu
    lgtrans["t{}".format(str(i).zfill(2))]['sla'] = sla
    lgtrans["t{}".format(str(i).zfill(2))]['bmode'] = bmode
    lgtrans["t{}".format(str(i).zfill(2))]['result'] = result
    lgtrans["t{}".format(str(i).zfill(2))]['tp_start'] = tp_start
    lgtrans["t{}".format(str(i).zfill(2))]['tp_end'] = tp_end


    with open("l_gtrans.json", "w") as outfile:
          json.dump(lgtrans, outfile, indent=4)





def create_reqinfo(ntrans):
    lreqinfo = {}
    i= 1
    provider=["p_77","p_98","p_90","p_93" ,"p_25","p_35","p_66" ,"p_26","p_46","p_95","p_12","p_86","p_20","p_43","p_22","p_82","p_38","p_94","p_58","p_76","p_53","p_72" ,"p_23","p_29","p_59","p_78","p_52","p_88","p_44","p_24","p_67","p_34","p_31","p_47","p_61","p_14","p_84","p_97" ,"p_56" ,"p_71","p_27","p_68","p_41","p_69","p_83","p_79","p_75","p_74","p_19","p_48","p_21","p_63" ,"p_87","p_17","p_13","p_89","p_18","p_81","p_92","p_45","p_28","p_15","p_11","p_96","p_62","p_60", "p_02" ,"p_03","p_04","p_05","p_06","p_07","p_08","p_09","p_10","p_49","p_50","p_30","p_42","p_37"]
    res_prod_sens= {"rp1":["p_77", "rp_07",8],
 "rp2":["p_98", "rp_05",8],
"rp3":["p_90", "rp_05",8],
"rp4":["p_93", "rp_02",1],
"rp5":["p_25", "rp_07",8],
"rp6":["p_35", "rp_06",1],
"rp7":["p_66", "rp_04",1],
"rp8":["p_26", "rp_06",8],
"rp9":["p_46", "rp_08",8],
"rp10":["p_95", "rp_05",8],
"rp11":["p_12", "rp_05",8],
"rp12":["p_86", "rp_09",1],
"rp13":["p_20", "rp_04",8],
"rp14":["p_43", "rp_08",8],
"rp15":["p_22", "rp_02",8],
"rp16":["p_82", "rp_02",5],
"rp17":["p_38", "rp_03",8],
"rp18":["p_94", "rp_04",8],
"rp19":["p_58", "rp_03",1],
"rp20":["p_76", "rp_02",1],
"rp21":["p_53", "rp_03",1],
"rp22":["p_72", "rp_02",5],
"rp23":["p_23", "rp_04",8],
"rp24":["p_29", "rp_05",8],
"rp25":["p_59", "rp_07",5],
"rp26":["p_78", "rp_04",5],
"rp27":["p_52", "rp_02",1],
"rp28":["p_88", "rp_07",8],
"rp29":["p_44", "rp_02",8],
"rp30":["p_24", "rp_02",5],
"rp31":["p_67", "rp_08",1],
"rp32":["p_34", "rp_02",8],
 "rp33":["p_31", "rp_07",1],
"rp34":["p_47", "rp_04",5],
"rp35":["p_61","rp_05",1],
"rp36":["p_14", "rp_05",8],
 "rp37":["p_84", "rp_06",8],
 "rp38":["p_97", "rp_04",8],
"rp39":["p_56", "rp_02",5],
"rp40":["p_71", "rp_03",5],
"rp41":["p_27", "rp_02",1],
 "rp42":["p_68", "rp_01",8],
"rp43":["p_41", "rp_08",8],
"rp44":["p_69", "rp_02",5],
 "rp45":["p_83", "rp_10",1],
 "rp46":["p_79", "rp_06",1],
 "rp47":["p_75", "rp_08",1],
"rp48":["p_74", "rp_06",8],
 "rp49":["p_19", "rp_08",5],
 "rp50":["p_48", "rp_10",1],
 "rp51":["p_50", "rp_07",5],
"rp52":["p_21", "rp_01",8],
 "rp53":["p_63", "rp_04",8],
 "rp54":["p_87", "rp_02",5],
 "rp55":["p_17", "rp_03",1],
"rp56":["p_13", "rp_09",8],
"rp57":["p_30", "rp_09",5],
"rp58":["p_89", "rp_04",5],
"rp59":["p_18", "rp_09",5],
 "rp60":["p_81", "rp_10",1],
 "rp61":["p_42", "rp_04",5],
 "rp62":["p_92", "rp_09",5],
 "rp63":["p_45", "rp_10",8],
 "rp64":["p_28", "rp_05",5],
 "rp65":["p_15", "rp_01",5],
 "rp66":["p_11", "rp_02",8],
 "rp67":["p_96", "rp_08",5],
 "rp68":["p_62", "rp_07",8],
"rp69":["p_60", "rp_07",1],
 "rp70":["p_02", "rp_04",1],
 "rp71":["p_03", "rp_08",5],
 "rp72":["p_04", "rp_03",5],
"rp73":["p_05", "rp_04",5],
"rp74":["p_06", "rp_06",8],
 "rp75":["p_07", "rp_04",5],
 "rp76":["p_08", "rp_02",8],
 "rp77":["p_37", "rp_03",1],
 "rp78":["p_09", "rp_01",5],
 "rp79":["p_10", "rp_07",1],
"rp80":["p_49", "rp_07",5]}
    litm=[]
    for item in res_prod_sens:
        litm.extend([[res_prod_sens[item][0], res_prod_sens[item][1], res_prod_sens[item][2]]])

    for _ in range(0, ntrans):
        random.shuffle(litm)
        rprovider=np.random.choice(provider)
        for it in litm:
            if it[0]!=rprovider:
                lreqinfo["req{}".format(str(i).zfill(2))] = {}
                lreqinfo["req{}".format(str(i).zfill(2))]['idu'] =rprovider
                lreqinfo["req{}".format(str(i).zfill(2))]['resource'] = it[1]
                lreqinfo["req{}".format(str(i).zfill(2))]['sensibility'] = it[2]
                lreqinfo["req{}".format(str(i).zfill(2))]['quantity'] = rand_data.random_int(1, 20)
                lreqinfo["req{}".format(str(i).zfill(2))]['date'] = str(rand_data.date_time())
                break


        i += 1


    with open("lreqinfo.json", "w") as outfile:
          json.dump(lreqinfo, outfile, indent=4)




def init_ltramperso(o_u):
    ltram={}

    with open("l_tram_"+o_u+".json", "w") as outfile:
          json.dump(ltram, outfile, indent=4)







def init_lrepm():
    i = 1
    l_resm = fjson_upload.fjon_import('l_resm.json')
    lrepm = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for repo in l_resm:

        lrepm["rep{}".format(str(i).zfill(2))] = {}
        lrepm["rep{}".format(str(i).zfill(2))]['id'] =l_resm[repo]["id"]
        lrepm["rep{}".format(str(i).zfill(2))]['resource'] = l_resm[repo]["resource"]
        lrepm["rep{}".format(str(i).zfill(2))]['sensibility'] = l_resm[repo]["sensibility"]
        lrepm["rep{}".format(str(i).zfill(2))]['specrep'] = 0
        i += 1

    lrepmjson = json.dumps(lrepm)

    with open("l_repm.json", "w") as outfile:
        json.dump(lrepm, outfile, indent=4)

    return lrepmjson



def init_lorgsd():
    l_resm = fjson_upload.fjon_import('l_resm.json')
    i = 1
    lorgsd = {}
    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = ["L", "M" , "H"]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}

    for item in l_resm:

        lorgsd["org{}".format(str(i).zfill(2))] = {}
        lorgsd["org{}".format(str(i).zfill(2))]['id'] = l_resm[item]["id"]
        lorgsd["org{}".format(str(i).zfill(2))]['secdomp'] = "L"
        lorgsd["org{}".format(str(i).zfill(2))]['globalrep'] = 0.5
        lorgsd["org{}".format(str(i).zfill(2))]['assurlevel'] = 0
        i += 1

    lorgsdjson = json.dumps(lorgsd)

    with open("l_orgsd.json", "w") as outfile:
        json.dump(lorgsd, outfile, indent=4)

    return lorgsdjson





def create_restrans(ldata,o_u,o_p,t_p,sd_u,sd_p,t_u,ttsp,sr_p,al_u,al_p,gr_u,gr_p):

    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}
    tl=len(ldata)

    i = tl + 1

    ldata["rdata{}".format(str(i).zfill(2))] = {}
    ldata["rdata{}".format(str(i).zfill(2))]['requester'] = o_u
    ldata["rdata{}".format(str(i).zfill(2))]['provider'] = o_p
    ldata["rdata{}".format(str(i).zfill(2))]['type_provider'] = t_p
    ldata["rdata{}".format(str(i).zfill(2))]['secdom_requester'] = sd_u
    ldata["rdata{}".format(str(i).zfill(2))]['secdom_provider'] = sd_p
    ldata["rdata{}".format(str(i).zfill(2))]['tvalue_requester'] = t_u
    ldata["rdata{}".format(str(i).zfill(2))]['tvalue_provider'] = ttsp
    ldata["rdata{}".format(str(i).zfill(2))]['specrep_provider'] = sr_p
    ldata["rdata{}".format(str(i).zfill(2))]['assurlevel_requester'] = al_u
    ldata["rdata{}".format(str(i).zfill(2))]['assurlevel_provider'] = al_p
    ldata["rdata{}".format(str(i).zfill(2))]['globrep_requester'] = gr_u
    ldata["rdata{}".format(str(i).zfill(2))]['globrep_provider'] = gr_p




    with open("info_restrans.json", "w") as outfile:
          json.dump(ldata, outfile, indent=4)





def create_nbdatatrans(ldata,nbg,nbm,nbv):

    StateFlagList = [0, 1]
    ResFlagList = ["rp_01", "rp_02","rp_03","rp_04","rp_05","rp_06","rp_07","rp_08","rp_09","rp_10"]
    Weight = [0.0, 1.0]
    SecdomFlagList = [1, 2, 3]
    SensdomFlagList = [8, 5, 1]
    Weightsens = [0.47, 0.33, 0.2]
    Weightsec = [0.47,0.33,0.2]
    Weightres = [0.08,0.15,0.10,0.2,0.08,0.08,0.08,0.08,0.08,0.07]
    #   lresm["or2g{}".format(str(i).zfill(2))] = {}
    tl=len(ldata)

    i = tl + 1

    ldata["stat{}".format(str(i).zfill(2))] = {}
    ldata["stat{}".format(str(i).zfill(2))]['nb_good'] = nbg
    ldata["stat{}".format(str(i).zfill(2))]['nb_viol'] = nbv
    ldata["stat{}".format(str(i).zfill(2))]['nb_malicious'] = nbm




    with open("nbdatatrans.json", "w") as outfile:
          json.dump(ldata, outfile, indent=4)


