import json

import int_assulev
import fjson_upload
import rep_value
import weight_share
import manag_data
import datetime
import os


l_repm = fjson_upload.fjon_importread('l_repm.json')
l_resm = fjson_upload.fjon_importread('l_resm.json')
l_datatnb = fjson_upload.fjon_importread("nbdatatrans.json")
alphai=0.5


# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary


def upd_value(o_p, o_u,t_p,res_share,t_rs,res,sens,qty,tts,ttsp, al_p,al_u,sd_u,sd_p,thresh):
    fileName = r"l_tram_"+o_u+".json"
    if os.path.isfile(fileName):
        l_trams = fjson_upload.fjon_importread("l_tram_" + o_u + ".json")
    else:
        donnees = {}
        with open("l_tram_" + o_u + ".json", "w") as file:
            json.dump(donnees, file)
        l_trams = fjson_upload.fjon_importread("l_tram_" + o_u + ".json")


    l_tram=l_trams
    l_gtrans = fjson_upload.fjon_importread("l_gtrans.json")
    l_orgsd = fjson_upload.fjon_importread("l_orgsd.json")
    l_datat = fjson_upload.fjon_importread("datatrans.json")
    info_restrans = fjson_upload.fjon_importread("info_restrans.json")
    t_org = fjson_upload.fjon_importread("ptpr.json")
    rp=""

    nbg=0
    nbm=0
    nbgn=0
    nbmn=0
    nborga=0

    t_out={}


    if t_p == 1:
        res_shareend = 1
    else:
        res_shareend = 0
    if res_shareend == 1 :
        sr_pn = rep_value.specrep_current(o_p) + rep_value.delta_upd(o_p,sens)
        al_pn = rep_value.assurlev_current(o_p) + rep_value.gamma_upd(o_p,sens)
        gr_pn = alphai + (weight_share.w_share(o_p) * rep_value.total_specrep(o_p))
        gr_un = alphai + (weight_share.w_share(o_u) * rep_value.total_specrep(o_u))
        sd_pn = int_assulev.security_domain(al_pn)
    elif res_shareend == 0.5 :
        sr_pn = rep_value.specrep_current(o_p) + (rep_value.delta_upd(o_p,sens)/2)
        al_pn = rep_value.assurlev_current(o_p) + (rep_value.gamma_upd(o_p,sens)/2)
        gr_pn = alphai + (weight_share.w_share(o_p) * rep_value.total_specrep(o_p))
        gr_un = alphai + (weight_share.w_share(o_u) * rep_value.total_specrep(o_u))
        sd_pn = int_assulev.security_domain(al_pn)
    else:
        sr_pn = rep_value.specrep_current(o_p) - rep_value.delta_upd(o_p,sens)
        al_pn = rep_value.assurlev_current(o_p) - rep_value.gamma_upd(o_p,sens)
        gr_pn = alphai + (weight_share.w_share(o_p) * rep_value.total_specrep(o_p))
        gr_un = alphai + (weight_share.w_share(o_u) * rep_value.total_specrep(o_u))
        sd_pn = int_assulev.security_domain(al_pn)


    j=1
    for itemo in t_org:
        if itemo==o_p:
            j=j*0
    if j==1:
        nborga=nborga+1
        t_org.append(o_p)
        with open('ptpr.json', 'w') as f:
            json.dump(t_org, f, indent=4)







    #  t_out.append(o_u)
    #  t_out.append(o_p)
    #  t_out.append(t_p)
    #  t_out.append(sd_pn)
    #   t_out.append(sd_u)
    #   t_out.append(tts)
    #   t_out.append(ttsp)
    #   t_out.append(sr_pn)
    #   t_out.append(al_pn)
    #   t_out.append(al_u)
    #   t_out.append(gr_pn)
    #   t_out.append(gr_un)

    t_out['requester']=o_u
    t_out['provider']=o_p
    t_out['type_provider']=t_p
    t_out['secdom_requester']=sd_pn
    t_out['secdom_provider']=sd_u
    t_out['tvalue_requester']=tts
    t_out['tvalue_provider']=ttsp
    t_out['specrep_provider']=sr_pn
    t_out['assurlevel_requester']=al_pn
    t_out['assurlevel_provider']=al_u
    t_out['globrep_requester']=gr_pn
    t_out['globrep_provider']=gr_un


    for rep in l_repm :
        if l_repm[rep]["id"]==o_p and l_repm[rep]["resource"]==res and l_repm[rep]["sensibility"]==sens:
            l_repm[rep]["specrep"] = sr_pn
            break
    with open('l_repm.json', 'w') as f:
        json.dump(l_repm, f, indent=4)

    for reso in l_resm :
        if l_resm[reso]["id"]==o_p and l_resm[reso]["resource"]==res and l_resm[reso]["sensibility"]==sens:
            if sd_pn=="H":
                l_resm[reso]["secdom"] = 3
            if sd_pn=="I":
                l_resm[reso]["secdom"] = 2
            if sd_pn=="L":
                l_resm[reso]["secdom"] = 1
            break
    with open('l_resm.json', 'w') as f:
        json.dump(l_resm, f, indent=4)



    for repo in l_orgsd:
        if l_orgsd[repo]["id"] == o_p:
            l_orgsd[repo]["globalrep"] = gr_pn
            l_orgsd[repo]["secdomp"] = sd_pn
            l_orgsd[repo]["assurlevel"] = al_pn
            break

    with open('l_orgsd.json', 'w') as f:
        json.dump(l_orgsd, f, indent=4)

    for repo in l_orgsd:
        if l_orgsd[repo]["id"] == o_u:
            l_orgsd[repo]["globalrep"] = gr_pn
            break

    with open('l_orgsd.json', 'w') as f:
        json.dump(l_orgsd, f, indent=4)



    ltramperso = manag_data.create_ltramperso(l_tram, o_u, o_p, res, sens, qty, tts, sr_pn, 1, 1, res_shareend,
                                              str(datetime.datetime.now()), str(datetime.datetime.now()))

    lgtranperso = manag_data.create_lgtransperso(l_gtrans, o_u, o_p, res, sens, qty, ttsp, tts, sr_pn, sd_pn, sd_u, 1,
                                                 1, res_shareend, str(datetime.datetime.now()),
                                                 str(datetime.datetime.now()))

    for dat in l_datat:
        if t_p == 1:
            l_datat[dat]["nbpg"] = l_datat[dat]["nbpg"] + 1
            l_datat[dat]["nborgpg"] = l_datat[dat]["nborgpg"] + nborga
            nbg=l_datat[dat]["nbpg"]
        else:
            l_datat[dat]["nbpm"] = l_datat[dat]["nbpm"] + 1
            l_datat[dat]["nborgpm"] = l_datat[dat]["nborgpm"] + nborga
            nbm = l_datat[dat]["nbpg"]
    with open('datatrans.json', 'w') as f:
        json.dump(l_datat, f, indent=4)

    datatrans = manag_data.create_restrans(info_restrans, o_u, o_p, t_p, sd_u, sd_pn, tts,ttsp,sr_pn, al_u, al_pn, gr_pn,
                                           gr_un)

    # nbstat=manag_data.create_nbdatatrans(l_datatnb,nbg,nbm,0)

    return t_out

"""modifier les valeurs dans un fichier"""
"""fournir les données en sortie json pour grafana"""
