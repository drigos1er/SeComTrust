import json


# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary


def fjon_import(fname):
    with open(fname) as json_file:
        lfile = json.load(json_file)
    return lfile

def fjon_importread(fnamer):
    with open(fnamer,"r") as json_filer:
        lfiler = json.load(json_filer)
    return lfiler


