import fjson_upload

"""Total transaction list"""
l_gtrans = fjson_upload.fjon_import('l_gtrans.json')
""" total number of transaction"""
nb_trans = (len(l_gtrans))


def total_trans():
    """
    total number of transaction
    :return: total number of transaction
    """
    return nb_trans


def total_transbyorg(org):
    """
    total number of transactions of an organization
    :param org: an organisation
    :return: total number of transactions
    """
    counttrans = 0
    for i in l_gtrans:
        if l_gtrans[i]["idp"] == org or l_gtrans[i]["idu"] == org:
            counttrans += 1

    return counttrans


def w_share(org):
    """
     weight of an organization's transactions
    :param org: an organisation
    :return: weight
    """
    if nb_trans==0:
        weight_share = 0
    else:
        weight_share = total_transbyorg(org) / nb_trans
    return weight_share


def tresult_transbetworg(o_p, o_u, res, sens, result):
    """
    total number of transactions  between organization according the result
    :param org: an organisation
    :return: number of transactions
    """
    p_t = 0
    for i in l_gtrans:
        if l_gtrans[i]["idp"] == o_p and l_gtrans[i]["idu"] == o_u and l_gtrans[i]["resource"] == res \
                and l_gtrans[i]["sensibility"] == sens and l_gtrans[i]["result"] == result:
            p_t += 1

    return p_t




def t_transbetworg(o_p, o_u, result):
    """
    total number of transactions  between organization according the result
    :param org: an organisation
    :return: number of transactions
    """
    p_t = 0
    for i in l_gtrans:
        if l_gtrans[i]["idp"] == o_p and l_gtrans[i]["idu"] == o_u  and l_gtrans[i]["result"] == result:
            p_t += 1

    return p_t

