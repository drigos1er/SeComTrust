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

def init_tram(o_u, o_p,t_p,res,sens,qty,tts,ttsp, al_p,al_u,sd_u,sd_p,thresh):
    l_resultshare = gov_matrix.resultpos_share(1, 1)
    upd = update_tvalues.upd_value( o_p, o_u,t_p,l_resultshare[0], l_resultshare[1],res,sens,qty,tts,ttsp, al_p,al_u,sd_u,sd_p,thresh)

    return upd





def init_rep(o_u, o_p,t_p,res,sens,qty,tts,ttsp, al_p,al_u,sd_u,sd_p,thresh):
    l_resultshare = gov_matrix.resultpos_share(1, 1)
    upd = update_tvalues.upd_value(o_p, o_u, t_p, l_resultshare[0], l_resultshare[1], res, sens, qty, tts, ttsp, al_p,al_u, sd_u, sd_p, thresh)

    return upd
