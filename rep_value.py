import fjson_upload
import int_assulev

"""specific reputation list"""
l_repm = fjson_upload.fjon_import('l_repm.json')
"""security domain and reputation global list"""
l_orgsd = fjson_upload.fjon_import('l_orgsd.json')
"""sla list"""
l_sla = fjson_upload.fjon_import('l_sla.json')


def total_specrep(org):
    """
    sum of the specific reputations of an organization
    :param org: an organisation
    :return: sum of the specific reputations
    """
    tspecrep = 0
    for item in l_repm:
        if l_repm[item]["id"] == org:
            tspecrep = tspecrep + l_repm[item]["specrep"]

    return tspecrep


def specrep_current(org):
    """
    current specific reputation
    :param org: an organisation
    :return: specific reputation
    """
    rep_spec = 0
    for i in l_repm:
        if l_repm[i]["id"] == org and l_repm[i]["sensibility"] and l_repm[i]["resource"]:
            spec_rep: float = l_repm[i]["specrep"]
            rep_spec = spec_rep
    return rep_spec


def assurlev_current(org):
    """
    current assurance level
    :param org: an organisation
    :return: assurance level
    """
    lev_ass = 0
    for i in l_orgsd:
        if l_orgsd[i]["id"] == org:
            ass_lev: float = l_orgsd[i]["assurlevel"]
            lev_ass = ass_lev
    return lev_ass


def gamma_upd(org,res_sens):
    """
    assurance level update value
    :param org: an oraganisation
    :return: update value
    """
    gam_upd: float = 0
    for i in l_orgsd:
        if l_orgsd[i]["id"] == org:
            lgamma = int_assulev.impact_share(l_orgsd[i]["secdomp"],res_sens)
            if l_orgsd[i]["assurlevel"] > 9.9:
                gam = 10 - l_orgsd[i]["assurlevel"]
            else:
                gam = lgamma[1]
            gam_upd = gam
    return gam_upd


def delta_upd(org,res_sens):
    """
    specifique reputation update value
    :param org: an organisation
    :return: update value
    """
    gdelt_is: float = 0
    for i in l_orgsd:
        if l_orgsd[i]["id"] == org:
            ldelta = int_assulev.impact_share(l_orgsd[i]["secdomp"],res_sens)
            gdelta_i = ldelta[1] * ldelta[0]
            gdelt_is = gdelta_i

    return gdelt_is


def global_rep(org):
    """
    global reputation value
    :param org: an organisation
    :return: global reputation
    """
    g_rep: float = 0
    for i in l_orgsd:
        if l_orgsd[i]["id"] == org:
            rep_g = l_orgsd[i]["globalrep"]
            g_rep = rep_g

    return g_rep


def sla_info(org_u, org_p, res_p, sen_resp, qty_u, date_u):
    """
    SLA transaction information
    :param org_u: Requesting organization
    :param org_p: Provider organization
    :param res_p: resource provided
    :param sen_resp: sensibility of resource provided
    :param qty_u: quantity provided
    :param date_u: wished date of delivery
    :return:
    """
    info_sla = []
    for it in l_sla:
        if l_sla[it]["idp"] == org_p and l_sla[it]["idu"] == org_u and l_sla[it]["resource"] == res_p \
                and l_sla[it]["sensibility"] == sen_resp and l_sla[it]["qtyu"] == qty_u and l_sla[it]["tp_u"] == date_u:
            info_sla = l_sla[it]
    return info_sla
