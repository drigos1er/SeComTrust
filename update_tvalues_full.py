import int_assulev

import rep_value
import weight_share

alphai=0.5


# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary


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

"""modifier les valeurs dans un fichier"""
"""fournir les données en sortie json pour grafana"""
