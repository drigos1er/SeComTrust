import datetime

import gov_matrix
import int_assulev

import update_tvalues
import rep_value

daydate = str(datetime.datetime.now())

# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary

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
                upd = update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                upd = update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)

        elif date_p <= date_d <= date_u:
            if av_init == 1:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                upd =  update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(0, 1)
                upd =  update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
        else:
            if av_init == 1:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                upd =   update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(0, 1)
                upd =   update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)

    return upd





def init_rep(o_u, o_p, trust_p, res_share, qty_u, qty_p, bm_u, bm_p, date_u, date_p, date_d, av_init, av_p,
              av_d):
    al_u = rep_value.assurlev_current(o_u)
    al_p = rep_value.assurlev_current(o_p)
    sd_u=int_assulev.security_domain(al_u)
    sd_p = int_assulev.security_domain(al_p)
    thresh = gov_matrix.der_thresh(sd_p,sd_u)
    if  trust_p >= thresh[0] and qty_u == qty_p and bm_u == bm_p:
        if (date_d <= date_p <= date_u) or (date_p >= date_u and date_p >= date_d):
            if av_init == 1 and daydate == date_d or av_init == 1 and av_d >= av_p:
                l_resultshare = gov_matrix.resultpos_share(1, 1)
                upd = update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                upd = update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)

        elif date_p <= date_d <= date_u:
            if av_init == 1:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                upd =  update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(0, 1)
                upd =  update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
        else:
            if av_init == 1:
                l_resultshare = gov_matrix.resultposvio_share(1, 1)
                upd =   update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)
            else:
                l_resultshare = gov_matrix.resultposvio_share(0, 1)
                upd =   update_tvalues.upd_value(l_resultshare[0], l_resultshare[0], o_p, o_u)

    return upd
