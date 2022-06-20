import provider_identification
import fjson_upload
import selectin_directtram
import selectin_foftram
import selectin_lrepm
import time

import manag_data

start = time.time()

req_inf = fjson_upload.fjon_import('req_info.json')
l_tram = fjson_upload.fjon_import('l_tram.json')
l_repm = fjson_upload.fjon_import('l_repm.json')
l_orgsd = fjson_upload.fjon_import('l_orgsd.json')

"""org_req = input('Quelle organisation demande la ressource ?')
res_req = input('Quelle est la ressourcée souhaitée ?')
sens_req = input('Quel est le niveau de sensibilité de la ressource souhaitée ?')
qty_req = input('Quelle est la quantité souhaitée ?')
date_req = input('A quelle date souhaite t\'elle disposer de la ressource  ?')"""

"""Resource provider identification"""

for req in req_inf:
    req_info = req_inf[req]
    try:
        lprovider = provider_identification.provider_id(req_info["idu"], req_info["resource"], req_info["sensibility"],
                                                        req_info["quantity"],
                                                        req_info["date"])

    except:
        print("ERREUR")

    else:
        if lprovider != []:

            try:
                l_tram = fjson_upload.fjon_import("l_tram_" + req_info["idu"] + ".json")

                direct_select = selectin_directtram.direct_tram(lprovider, l_tram, req_info["idu"],
                                                                req_info["resource"],
                                                                req_info["sensibility"],
                                                                req_info["quantity"], req_info["date"])
                if direct_select:
                    print(direct_select)
                    end = time.time()
                else:
                    fof_select = selectin_foftram.fof_tram(lprovider, l_tram, req_info["idu"], req_info["resource"],
                                                           req_info["sensibility"],
                                                           req_info["quantity"], req_info["date"])
                    if fof_select:
                        print(fof_select)
                        end = time.time()
                    else:

                        rep_select = selectin_lrepm.s_lrepm(lprovider, l_repm, l_orgsd, req_info["idu"],
                                                            req_info["resource"],
                                                            req_info["sensibility"],
                                                            req_info["quantity"], req_info["date"])
                        if rep_select:
                            print(rep_select)
                            end = time.time()
                        else:
                            end = time.time()
                            print("AUCUN FOURNISSEUR IDENTIFIE")
            except:

                rep_select = selectin_lrepm.s_lrepm(lprovider, l_repm, l_orgsd, req_info["idu"], req_info["resource"],
                                                    req_info["sensibility"],
                                                    req_info["quantity"], req_info["date"])
                if rep_select:
                    print(rep_select)
                    end = time.time()
                else:
                    end = time.time()
                    print("AUCUN FOURNISSEUR IDENTIFIE")




        else:
            end = time.time()

            print("AUCUN FOURNISSEUR IDENTIFIE")





