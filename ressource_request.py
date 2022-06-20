def res_request():
    req_info=[]
    org_req=input ('Quelle organisation demande la ressource ?')
    res_req = input('Quelle est la ressourcée souhaitée ?')
    sens_req = input('Quel est le niveau de sensibilité de la ressource souhaitée ?')
    qty_req = input('Quelle est la quantité souhaitée ?')
    date_req = input('A quelle date souhaite t\'elle disposer de la ressource  ?')

    req_info.append(org_req)
    req_info.append(res_req)
    req_info.append(sens_req)
    req_info.append(qty_req)
    req_info.append(date_req)

    return req_info


