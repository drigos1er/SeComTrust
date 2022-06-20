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
    tts = ""
    ttsp = ""
    org = ""
    for item in l_rpsdesc:
        for rep in l_repm:
            if item[0] == l_repm[rep]["id"] and des_res == l_repm[rep][
                "resource"] and l_repm[rep]["sensibility"] == sens_res and l_repm[rep]["specrep"] > 0:

                org_specrep.extend([[l_repm[rep]["id"], l_repm[rep]["specrep"], o_u, des_res, sens_res, qty_res, date_res]])
                break
    l_specrepdesc = sorted(org_specrep, key=operator.itemgetter(1), reverse=True)

    if l_specrepdesc:
        for itsp in l_specrepdesc:

            trust_pu = rep_value.global_rep(o_u)
            l_slainf = rep_value.sla_info(o_u, itsp[0], des_res, sens_res, qty_res, date_res)
            al_u = rep_value.assurlev_current(o_u)
            al_p = rep_value.assurlev_current(itsp[0])
            sd_u = int_assulev.security_domain(al_u)
            sd_p = int_assulev.security_domain(al_p)
            thresh = gov_matrix.der_thresh(sd_p, sd_u)

            if  trust_pu >= thresh[0] and l_slainf['qtyu'] == l_slainf['qtyp'] and l_slainf[
                'bmodeu'] == l_slainf['bmodep']:
                trans_inits = l_slainf

                ttsp = trust_pu

                trans_init = valini_tram.init_rep(trans_inits['idu'], trans_inits['idp'],  ttsp,
                                                   trans_inits['resource'], trans_inits['qtyu'], trans_inits['qtyp'],
                                                   trans_inits['bmodeu'], trans_inits['bmodep'], trans_inits['tp_u'],
                                                   trans_inits['tp_p'],
                                                   trans_inits['tp_d'], trans_inits['availlable_init'],
                                                   trans_inits['availlable_p'],
                                                   trans_inits['availlable_d'])

                break

        return trans_init
    else :
        for item in l_rpsdesc:
            for grep in l_orgsd:
                if item[0] == l_orgsd[grep]["id"]:
                    org_grep.extend(
                        [[l_orgsd[grep]["id"], l_orgsd[grep]["globalrep"], o_u, des_res, sens_res, qty_res, date_res]])
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

                if trust_pu >= thresh[0] and l_slainf['qtyu'] == l_slainf['qtyp'] and l_slainf[
                    'bmodeu'] == l_slainf['bmodep']:
                    trans_inits = l_slainf

                    ttsp = trust_pu

                    trans_init = valini_tram.init_rep(trans_inits['idu'], trans_inits['idp'], ttsp,
                                                      trans_inits['resource'], trans_inits['qtyu'], trans_inits['qtyp'],
                                                      trans_inits['bmodeu'], trans_inits['bmodep'], trans_inits['tp_u'],
                                                      trans_inits['tp_p'],
                                                      trans_inits['tp_d'], trans_inits['availlable_init'],
                                                      trans_inits['availlable_p'],
                                                      trans_inits['availlable_d'])

                    break

            return trans_init



