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

import update_tvalues
import rep_value

daydate = str(datetime.datetime.now())


def direct_tram(l_rpsdesc, l_tram, o_u, des_res, sens_res, qty_res, date_res):
    alpha_i = 0.5
    trans_init=[]
    org_direct=[]
    tts = ""
    ttsp = ""
    al_ps = ""
    al_pu=""
    sd_us = ""
    sd_ps = ""
    org=""
    tt1=""
    tt2=""
    tt = ""
    for item in l_rpsdesc:
        for transact in l_tram:
            if (item[0] == l_tram[transact]["id"] and des_res == l_tram[transact][
                "resource"] and l_tram[transact]["sensibility"] ==
                sens_res) or (item[0] == l_tram[transact]["id"]  and l_tram[transact]["sensibility"] >=
                              sens_res):

                org_direct.append([l_tram[transact]["id"],item[1],item[2]])
                break

    for it in org_direct:

        p_t = weight_share.tresult_transbetworg(it[0], o_u, des_res, sens_res, 1)
        n_t = weight_share.tresult_transbetworg(it[0], o_u, des_res, sens_res, 0)
        bel = p_t / (p_t + n_t + 2)
        uncert = 2 / (p_t + n_t + 2)
        drt = bel + (alpha_i * uncert)
        tt = 0.6 * drt + 0.4 * rep_value.specrep_current(it[0])
        trust_up = tt
        trust_pu = rep_value.global_rep(o_u)
        l_slainf = rep_value.sla_info(o_u, it[0], des_res, sens_res, qty_res, date_res)
        al_u = rep_value.assurlev_current(o_u)

        al_p = rep_value.assurlev_current(it[0])

        sd_u = int_assulev.security_domain(al_u)

        sd_p = int_assulev.security_domain(al_p)

        thresh = gov_matrix.der_thresh(sd_p, sd_u)

        if trust_up >= thresh[1] and trust_pu >= thresh[0]:
            trans_inits = l_slainf
            tts = trust_up
            ttsp = trust_pu
            org = it[0]
            trans_init = valini_tram.init_tram(o_u, it[0],it[2],des_res, sens_res,qty_res, tts, ttsp, al_p,al_u,sd_u,sd_p,thresh)

            break
    return trans_init





