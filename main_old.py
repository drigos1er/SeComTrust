import provider_identification
import fjson_upload
import selectin_directtram
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
import datetime

import gov_matrix
import int_assulev

import update_tvalues
import rep_value

import int_assulev

import rep_value
import weight_share

alphai=0.5




# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary

req_info = fjson_upload.fjon_import('req_info.json')
l_tram = fjson_upload.fjon_import('l_tram.json')

"""org_req = input('Quelle organisation demande la ressource ?')
res_req = input('Quelle est la ressourcée souhaitée ?')
sens_req = input('Quel est le niveau de sensibilité de la ressource souhaitée ?')
qty_req = input('Quelle est la quantité souhaitée ?')
date_req = input('A quelle date souhaite t\'elle disposer de la ressource  ?')"""




def upd_value(res_share, t_rs, o_p, o_u):
    t_out=[]
    if res_share == 1 and t_rs == 1:
        sr_p = rep_value.specrep_current(o_p) + rep_value.delta_upd(o_p)
        al_p = rep_value.assurlev_current(o_p) + rep_value.gamma_upd(o_p)
        gr_p = alphai + (weight_share.w_share(o_p) * rep_value.total_specrep(o_p))
        gr_u = alphai + (weight_share.w_share(o_u) * rep_value.total_specrep(o_u))
        sd_p = int_assulev.security_domain(al_p)
    elif res_share == 1 and t_rs == 0.5:
        sr_p = rep_value.specrep_current(o_p) + (rep_value.delta_upd(o_p) / 2)
        al_p = rep_value.assurlev_current(o_p) + (rep_value.gamma_upd(o_p) / 2)
        gr_p = alphai + weight_share.w_share(o_p) * rep_value.total_specrep(o_p)
        gr_u = alphai + weight_share.w_share(o_u) * rep_value.total_specrep(o_u)
        sd_p = int_assulev.security_domain(al_p)
    else:
        sr_p = rep_value.specrep_current(o_p) - rep_value.delta_upd(o_p)
        al_p = rep_value.assurlev_current(o_p) - rep_value.gamma_upd(o_p)
        gr_p = alphai + weight_share.w_share(o_p) * rep_value.total_specrep(o_p)
        gr_u = alphai + weight_share.w_share(o_u) * rep_value.total_specrep(o_u)
        sd_p = int_assulev.security_domain(al_p)
    t_out.append(sr_p)
    t_out.append(al_p)
    t_out.append(gr_p)
    t_out.append(gr_u)
    t_out.append(sd_p)
    t_out.append(o_u)
    t_out.append(o_p)

    return t_out






def init_tram(o_u, o_p, trust_u, trust_p, res_share, qty_u, qty_p, bm_u, bm_p, date_u, date_p, date_d, av_init, av_p,
              av_d):
    al_u = rep_value.assurlev_current(o_u)
    al_p = rep_value.assurlev_current(o_p)
    sd_u=int_assulev.security_domain(al_u)
    sd_p = int_assulev.security_domain(al_p)
    thresh = gov_matrix.der_thresh(sd_p,sd_u)
    if trust_u >= thresh[1] and trust_p >= thresh[0] and qty_u == qty_p and bm_u == bm_p:
        if (date_d <= date_p <= date_u) or (date_p >= date_u and date_p >= date_d):
            if av_init == 1 and daydate == date_d or av_init == 1 and av_d >= av_p:
                l_resultshare = gov_matrix.resultpos_share(1, 1)
                update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)

        elif date_p <= date_d <= date_u:
            if av_init == 1:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(0, 1)
                update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
        else:
            if av_init == 1:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(0, 1)
                update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)





def direct_tram(l_rpsdesc, l_tram, o_u, des_res, sens_res, qty_res, date_res):
    alpha_i = 0.5
    trans_inits=[]
    org_direct=[]
    tts = ""
    ttsp = ""
    org=""
    for item in l_rpsdesc:
        for transact in l_tram:
            if (item[0] == l_tram[transact]["id"] and des_res == l_tram[transact][
                "resource"] and l_tram[transact]["sensibility"] ==
                sens_res) or (item[0] == l_tram[transact]["id"]  and l_tram[transact]["sensibility"] >=
                              sens_res):

                org_direct.append([l_tram[transact]["id"],item[1]])
                break

    for it in org_direct:

        p_t = weight_share.tresult_transbetworg(it[0], o_u, des_res, sens_res, 1)
        n_t = weight_share.tresult_transbetworg(it[0], o_u, des_res, sens_res, 0)
        bel = p_t / (p_t + n_t + 2)
        uncert = 2 / (p_t + n_t + 2)
        drt = bel + (alpha_i * uncert)
        tt = 0.7 * drt + 0.3 * rep_value.specrep_current(it[0])
        trust_up = tt
        trust_pu = rep_value.global_rep(o_u)
        l_slainf = rep_value.sla_info(o_u, it[0], des_res, sens_res, qty_res, date_res)
        al_u = rep_value.assurlev_current(o_u)
        al_p = rep_value.assurlev_current(it[0])
        sd_u = int_assulev.security_domain(al_u)
        sd_p = int_assulev.security_domain(al_p)
        thresh = gov_matrix.der_thresh(sd_p, sd_u)

        if trust_up >= thresh[1] and trust_pu >= thresh[0] and l_slainf['qtyu'] == l_slainf['qtyp'] and l_slainf['bmodeu'] == l_slainf['bmodep']:
            trans_inits=l_slainf
            tts=trust_up
            ttsp=trust_pu
            org=it[0]
            break
    trans_init = init_tram(trans_inits['idu'], trans_inits['idp'], tts, ttsp,
                                      trans_inits['resource'], trans_inits['qtyu'], trans_inits['qtyp'],
                                      trans_inits['bmodeu'], trans_inits['bmodep'], trans_inits['tp_u'],
                                      trans_inits['tp_p'],
                                      trans_inits['tp_d'], trans_inits['availlable_init'],
                                      trans_inits['availlable_p'],
                                      trans_inits['availlable_d'])

    return trans_init










try:
    lprovider = provider_identification.provider_id(req_info["org"], req_info["res"], req_info["sens"], req_info["qty"],
                                                    req_info["date"])

except:
    print("ERREUR")

else:
    if lprovider != []:
        direct_select = direct_tram(lprovider, l_tram, req_info["org"], req_info["res"],
                                                        req_info["sens"],
                                                        req_info["qty"], req_info["date"])

        print(direct_select)


    else:
        print("AUCUN FOURNISSEUR IDENTIFIE")










# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary



"""modifier les valeurs dans un fichier"""
"""fournir les données en sortie json pour grafana"""



"""Resource provider identification"""



