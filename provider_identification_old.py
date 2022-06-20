import fjson_upload
import operator

l_rps = []
# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary

l_resm = fjson_upload.fjon_import('l_resm.json')


def provider_id(o_u, des_res, sens_res, qty_res, date_res):
    """
    identification of the provider of the requested resource
    :param desired_res: requested resource
    :param sensibility_res: resource sensibility
    :param quantity_res: resource quantity
    :param l_resm: resource list
    :return: list of providers
    """
    for item in l_resm:
        # la variable item va contenir chacun des dictionnaires
        if des_res == l_resm[item]["resource"] and \
                sens_res == l_resm[item]["sensibility"] \
                and l_resm[item]["available"] >= qty_res:
            l_rps.extend([[l_resm[item]["id"], l_resm[item]["secdom"], o_u, des_res, sens_res, qty_res, date_res]])


    l_rpsdesc = sorted(l_rps, key=operator.itemgetter(1), reverse=True)
    return l_rpsdesc


