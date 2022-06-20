import fjson_upload
import operator

l_rps = []
# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary

l_resm = fjson_upload.fjon_import('l_resm.json')
l_orgsd = fjson_upload.fjon_import('l_orgsd.json')
l_req = fjson_upload.fjon_import('lreqinfo_t500_1.json')


def provider_id(o_u, des_res, sens_res, qty_res, date_res):
    """
    identification of the provider of the requested resource
    :param desired_res: requested resource
    :param sensibility_res: resource sensibility
    :param quantity_res: resource quantity
    :param l_resm: resource list
    :return: list of providers
    """
    assurlevel=0
    for item in l_resm:
        # la variable item va contenir chacun des dictionnaires
        if des_res == l_resm[item]["resource"] and \
                sens_res == l_resm[item]["sensibility"]:
            for al in l_orgsd:
                if l_resm[item]["id"] == l_orgsd[al]["id"]:
                    assurlevel = l_orgsd[al]["assurlevel"]
                    break
            l_rps.extend([[l_resm[item]["id"], l_resm[item]["secdom"],l_resm[item]["typep"],assurlevel, o_u, des_res, sens_res, qty_res, date_res]])


    l_rpsdesc = sorted(l_rps, key=operator.itemgetter(1,3), reverse=True)
    return l_rpsdesc


def lresm_id():
    print(l_req)
lresm_id()



