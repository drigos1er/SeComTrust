import provider_identification
import rep_value
import valini_tram
# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary
import weight_share
import datetime

import gov_matrix
import int_assulev
import operator
import update_tvalues
import rep_value
import fjson_upload

daydate = str(datetime.datetime.now())



def s_lrepm(l_rpsdesc, l_repm,l_orgsd, o_u, des_res, sens_res, qty_res, date_res):
    alpha_i = 0.5
    trans_init = []
    org_specrep = []
    org_grep = []
    globalrep=0
    tts = ""
    ttsp = ""
    org = ""
    for item in l_rpsdesc:
        for rep in l_repm:
            if item[0] == l_repm[rep]["id"] and des_res == l_repm[rep][
                "resource"] and l_repm[rep]["sensibility"] == sens_res and l_repm[rep]["specrep"] > 0:

                org_specrep.extend([[l_repm[rep]["id"], l_repm[rep]["specrep"], item[2], o_u, des_res, sens_res, qty_res, date_res]])
                break
    l_specrepdesc = sorted(org_specrep, key=operator.itemgetter(1), reverse=True)

    if l_specrepdesc:
        for itsp in l_specrepdesc:

            trust_pu = rep_value.global_rep(o_u)
            #l_slainf = rep_value.sla_info(o_u, itsp[0], des_res, sens_res, qty_res, date_res)
            al_u = rep_value.assurlev_current(o_u)
            al_p = rep_value.assurlev_current(itsp[0])
            sd_u = int_assulev.security_domain(al_u)
            sd_p = int_assulev.security_domain(al_p)
            thresh = gov_matrix.der_thresh(sd_p, sd_u)



            if  trust_pu >= thresh[0] :
                #trans_inits = l_slainf

                tts = alpha_i
                ttsp = trust_pu

                trans_init = valini_tram.init_rep(o_u, itsp[0],itsp[2],des_res, sens_res, qty_res,tts,ttsp, al_p, al_u, sd_u, sd_p, thresh)

                break

        return trans_init
    else :
        for ite in l_rpsdesc:
            for repo in l_repm:
                if ite[0] == l_repm[repo]["id"] and des_res == l_repm[repo][
                    "resource"] and l_repm[repo]["sensibility"] == sens_res:
                    for grep in l_orgsd:
                        if ite[0] == l_orgsd[grep]["id"]:
                            globalrep=l_orgsd[grep]["globalrep"]
                            break
                    org_grep.extend(
                        [[ite[0],globalrep,ite[2], o_u, des_res, sens_res, qty_res, date_res]])
                    break
        l_grepdesc = sorted(org_grep, key=operator.itemgetter(1), reverse=True)

        if l_grepdesc:
            for itg in l_grepdesc:

                trust_pu = rep_value.global_rep(o_u)
                l_slainf = rep_value.sla_info(o_u, itg[0], des_res, sens_res, qty_res, date_res)
                al_u = rep_value.assurlev_current(o_u)
                al_p = rep_value.assurlev_current(itg[0])
                sd_u = int_assulev.security_domain(al_u)
                sd_p = int_assulev.security_domain(al_p)
                thresh = gov_matrix.der_thresh(sd_p, sd_u)
                if trust_pu >= thresh[0]:
                    # trans_inits = l_slainf
                    tts = alpha_i

                    ttsp = trust_pu

                    trans_init = valini_tram.init_rep(o_u, itg[0], itg[2], des_res, sens_res, qty_res, tts, ttsp,
                                                      al_p, al_u, sd_u, sd_p, thresh)



                    break

            return trans_init



