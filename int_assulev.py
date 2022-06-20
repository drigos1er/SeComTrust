import numpy as np

l_impacts = []
""" security insurance interval"""
ass_level = np.array([[0, 3.99], [4, 6.99], [7, 10]])
"""transaction weight matrix"""
gamma_i = np.array([0.2, 0.35, 0.45])

def deduct_gammai(res_sens):
    gammi=0
    if 0<= res_sens < 4:
        gammi=gamma_i[2]
    if 4<= res_sens < 7:
        gammi = gamma_i[1]
    if 7 <= res_sens <= 10:
        gammi = gamma_i[0]
    return gammi




def impact_share(sd_p,res_sens):
    """
    Weight of a transaction according to the security domain of the provider
    :param sd_p: the security domain of the provider
    :return:list of the weight of the provider's security insurance interval
    and Weight of according to the security domain of the provider
    """
    if sd_p == "H":
        delta_i = ((ass_level[2][0] + ass_level[2][1]) / 2) / ass_level[2][1]
        gam_i = deduct_gammai(res_sens)
        l_impacts.append(delta_i)
        l_impacts.append(gam_i)
    if sd_p == "I":
        delta_i = ((ass_level[1][0] + ass_level[1][1]) / 2) / ass_level[2][1]
        gam_i = deduct_gammai(res_sens)
        l_impacts.append(delta_i)
        l_impacts.append(gam_i)
    if sd_p == "L":
        delta_i = ((ass_level[0][0] + ass_level[0][1]) / 2) / ass_level[2][1]
        gam_i = deduct_gammai(res_sens)
        l_impacts.append(delta_i)
        l_impacts.append(gam_i)
    return l_impacts


def security_domain(al_p):
    """
    Derivation of security domain based on assurance level
    :param al_p:assurance level
    :return: secuity domain
    """
    if al_p < ass_level[1][0]:
        sd_org = "L"
    elif ass_level[1][0] <= al_p < ass_level[2][0]:
        sd_org = "I"
    else:
        sd_org = "H"
    return sd_org

