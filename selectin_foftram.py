import provider_identification
import rep_value
import valini_tram
import fjson_upload
# with open("l_resm.json", "w") as outfile:
# json.dump(l_resm, outfile)
# Opening JSON file
# openning and convert json file in dictionnary
import weight_share
import datetime

import gov_matrix
import int_assulev
import os

import update_tvalues
import rep_value

daydate = str(datetime.datetime.now())


def produituncer(item, l_rec):
    pu = 1
    for it in l_rec:
        if it != item:
            pu = pu * l_rec[it][5]
    return pu


def beluncer(item, l_rec):
    pu = produituncer(item, l_rec)
    belun = 0
    for it in l_rec:
        if it == item:
            belun = pu * l_rec[it][3]
    return belun


def numeratorop(l_rec):
    numerop = 0
    for it in l_rec:
        bu = beluncer(it, l_rec)

        numerop = numerop + bu
    return numerop


def sommuncer(l_rec):
    sun = 0
    for it in l_rec:
        sun = sun + l_rec[it][5]
    return sun


def totalproduituncer(l_rec):
    pu = 1
    for it in l_rec:
        pu = pu * l_rec[it][5]
    return pu


def denomop(l_rec):
    sun = sommuncer(l_rec)
    tprodun = totalproduituncer(l_rec)
    denomop = sun - tprodun

    return denomop


def disuncer(item, l_rec):
    pu = produituncer(item, l_rec)
    disun = 0
    for it in l_rec:
        if it == item:
            disun = pu * l_rec[it][4]
    return disun


def numeratordis(l_rec):
    numerop = 0
    for it in l_rec:
        du = disuncer(it, l_rec)
        numerop = numerop + du
    return numerop


def fof_tram(l_rpsdesc, l_tram, o_u, des_res, sens_res, qty_res, date_res):
    alpha_i = 0.5
    trans_init = []
    org_fof = []
    l_recom = []
    l_fof = []
    tts = ""
    ttsp = ""
    org = ""

    v_rec = []
    tvalue_rec = {}
    for transact in l_tram:
        # Vérifier si une organisation de la liste de transaction du demandeur a fourni une ressource différente avec niveau de sensibilité superieur à ce qui est demandé
        if des_res != l_tram[transact]["resource"] and int(l_tram[transact]["sensibility"]) > sens_res:
            # Enregister les organisations dans une liste temporaire si elle n'y est pas déja
            if l_tram[transact]["id"] not in org_fof:
                org_fof.append(l_tram[transact]["id"])

    # Parcourir maintenant les fournisseurs identifés de la ressource
    for item in l_rpsdesc:
        # Parcourir la liste des amis du demandeur selectionné
        n = 0
        for orgi in org_fof:
            # Chargé la  liste de transaction de l'ami courant du demandeur
            l_trami = fjson_upload.fjon_import('l_trami.json')
            fileName = r"l_tram_" + orgi + ".json"
            if os.path.isfile(fileName):
                l_trami = fjson_upload.fjon_importread("l_tram_" + orgi + ".json")
            else:
                trans_init = []
                continue


# Verifier dans cette liste de transaction du demandeur courant s'il y a un échange pour la même transaction

            for trani in l_trami:
                if item[0] == l_trami[trani]["id"] and des_res == l_trami[trani][
                    "resource"] and l_trami[trani]["sensibility"] == sens_res:
                    n = n + 1
                    l_recom.append([orgi])
                    break

        if n == 1:  # ona un seul ami donc on est dans un contexte de FOF
            for rec in l_recom:
                pglogal_tur = weight_share.t_transbetworg(rec[0], o_u, 1)
                nglobal_tur = weight_share.t_transbetworg(rec[0], o_u, 0)
                belur = pglogal_tur / (pglogal_tur + nglobal_tur + 2)
                dislur = nglobal_tur / (pglogal_tur + nglobal_tur + 2)
                uncertur = 2 / (pglogal_tur + nglobal_tur + 2)

                p_trp = weight_share.tresult_transbetworg(item[0], rec[0], des_res, sens_res, 1)
                n_trp = weight_share.tresult_transbetworg(item[0], rec[0], des_res, sens_res, 0)
                belrp = p_trp / (p_trp + n_trp + 2)
                dislrp = n_trp / (p_trp + n_trp + 2)
                uncertrp = 2 / (p_trp + n_trp + 2)

                belup = belur * belrp
                disup = belur * dislrp
                uncertup = dislur + uncertur + belur * uncertrp

                drtup = belup + (alpha_i * uncertup)
                tt = 0.6 * drtup + 0.4 * rep_value.specrep_current(item[0])
                trust_up = tt
                trust_pu = rep_value.global_rep(o_u)
                l_slainf = rep_value.sla_info(o_u, item[0], des_res, sens_res, qty_res, date_res)
                al_u = rep_value.assurlev_current(o_u)
                al_p = rep_value.assurlev_current(item[0])
                sd_u = int_assulev.security_domain(al_u)
                sd_p = int_assulev.security_domain(al_p)
                thresh = gov_matrix.der_thresh(sd_p, sd_u)

                if trust_up >= thresh[1] and trust_pu >= thresh[0]:
                    trans_inits = l_slainf
                    tts = trust_up
                    ttsp = trust_pu
                    org = item[0]
                    trans_init = valini_tram.init_tram(o_u, item[0], item[2], des_res, sens_res, qty_res, tts, ttsp,
                                                       al_p,
                                                       al_u, sd_u, sd_p, thresh)
            break
        elif n > 1:

            for rec in l_recom:
                pglogal_tur = weight_share.t_transbetworg(rec[0], o_u, 1)
                nglobal_tur = weight_share.t_transbetworg(rec[0], o_u, 0)
                belur = pglogal_tur / (pglogal_tur + nglobal_tur + 2)
                dislur = nglobal_tur / (pglogal_tur + nglobal_tur + 2)
                uncertur = 2 / (pglogal_tur + nglobal_tur + 2)

                p_trp = weight_share.tresult_transbetworg(item[0], rec[0], des_res, sens_res, 1)
                n_trp = weight_share.tresult_transbetworg(item[0], rec[0], des_res, sens_res, 0)
                belrp = p_trp / (p_trp + n_trp + 2)
                dislrp = n_trp / (p_trp + n_trp + 2)
                uncertrp = 2 / (p_trp + n_trp + 2)

                v_rec.append([belur, dislur, uncertur, belrp, dislrp, uncertrp])

            # tvalue_rec = {'org01': [0.0, 0.0, 1.0, 4.0, 3.0, 2.0], 'org02': [0.0, 0.0, 1.0, 5.0, 4.0, 2.0], 'org03': [0.0, 0.0, 1.0, 5.0, 4.0, 2.0]}

            i = 1

            for element in v_rec:
                tvalue_rec["org{}".format(str(i).zfill(2))] = element
                i += 1


            numerator = numeratorop(tvalue_rec)
            numeratodisl = numeratordis(tvalue_rec)
            denominator = denomop(tvalue_rec)
            belief = numerator / denominator
            dislief = numeratodisl / denominator
            uncert = totalproduituncer(tvalue_rec) / denominator

            drt = belief + (alpha_i * uncert)
            tt = 0.6 * drt + 0.4 * rep_value.specrep_current(item[0])
            trust_up = tt
            trust_pu = rep_value.global_rep(o_u)
            l_slainf = rep_value.sla_info(o_u, item[0], des_res, sens_res, qty_res, date_res)
            al_u = rep_value.assurlev_current(o_u)
            al_p = rep_value.assurlev_current(item[0])
            sd_u = int_assulev.security_domain(al_u)
            sd_p = int_assulev.security_domain(al_p)
            thresh = gov_matrix.der_thresh(sd_p, sd_u)

            if trust_up >= thresh[1] and trust_pu >= thresh[0]:
                trans_inits = l_slainf
                tts = trust_up
                ttsp = trust_pu
                org = item[0]
                trans_init = valini_tram.init_tram(o_u, item[0], item[2], des_res, sens_res, qty_res, tts, ttsp,
                                                   al_p,
                                                   al_u, sd_u, sd_p, thresh)

                break
        else:
            trans_init = []

    return trans_init























