import json


# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary


def fjon_importread(fname):
    with open(fname,"r") as json_file:
        lfile = json.load(json_file)
    return lfile


