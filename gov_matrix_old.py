import numpy as np

l_thresh = []
l_reshare = []

prov_gov = np.array([[0.8, 0.7, 0.5], [0.8, 0.7, 0.5], [0.8, 0.7, 0.5]])
usr_gov = np.array([[0.7, 0.5, 0.3], [0.7, 0.5, 0.3], [0.7, 0.5, 0.3]])




def der_thresh(sd_p, sd_u):
    if sd_p == "H":
        if sd_u == "H":
            t_p = prov_gov[2][2]
            t_u = usr_gov[2][2]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
        if sd_u == "I":
            t_p = prov_gov[2][1]
            t_u = usr_gov[1][2]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
        if sd_u == "L":
            t_p = prov_gov[2][0]
            t_u = usr_gov[0][2]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
    if sd_p == "I":
        if sd_u == "H":
            t_p = prov_gov[1][2]
            t_u = usr_gov[2][1]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
        if sd_u == "I":
            t_p = prov_gov[1][1]
            t_u = usr_gov[1][1]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
        if sd_u == "L":
            t_p = prov_gov[1][0]
            t_u = usr_gov[0][1]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
    if sd_p == "L":
        if sd_u == "H":
            t_p = prov_gov[0][2]
            t_u = usr_gov[2][0]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
        if sd_u == "I":
            t_p = prov_gov[0][1]
            t_u = usr_gov[1][0]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
        if sd_u == "L":
            t_p = prov_gov[0][0]
            t_u = usr_gov[0][0]
            l_thresh.append(t_p)
            l_thresh.append(t_u)
    return l_thresh


def resultpos_share(feedback_u, feedback_p):
    if feedback_u == 1 and feedback_p == 1:
        result_s = 1
        slaresult_s = 1
        l_reshare.append(result_s)
        l_reshare.append(slaresult_s)
    return l_reshare


def resultposvio_share(feedback_u, feedback_p):
    if feedback_u == 1 and feedback_p == 1:
        result_s = 1
        slaresult_s = 0.5
        l_reshare.append(result_s)
        l_reshare.append(slaresult_s)
    return l_reshare


def resultneg_share(feedback_u, feedback_p):
    if feedback_u != 1 and feedback_p != 1:
        result_s = 0
        slaresult_s = 0
        l_reshare.append(result_s)
        l_reshare.append(slaresult_s)
    return l_reshare
