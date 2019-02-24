u"""

"""
import os
import requests

endpoint = os.environ.get('APIURL')


def get_total(periodos, type):
    # lista de todos los clientes vacia
    total = []

    for periodo, fecha in periodos.items():
        # por cada periodo se obtienen la fecha inicial y final
        response = requests.get(
            # se pasan las fechas al endpoint como parametros
            endpoint+'/'+type+'/'+fecha['start']+'/'+fecha['end']
            # se obtiene la respuesta en formato json
        ).json()

        for item in response:
            # por cada elemento (cliente) en la respuesta
            # se agregan al listado total
            total.append(item)

    # se regresa el listado de todos los clientes
    return total


def posts_results(resume):
    r = requests.post(endpoint+'/conta/resumen', json=resume)
    print(r.text)
