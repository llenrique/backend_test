u""".

Problema:
    Se debe obtener un listado de todos los clientes (los cuales se dieron de
    alta en 2017)

Descripción:
    Trae un listado de los usuarios que fueron creados entre las fechas de
    inicio y fin.

    Las fechas deben estar en formato YYYY-MM-DD.

    Si hay más de 50 resultados en el rango de fechas, contestará con la
    leyenda "Hay más de 50 elementos" y un status 406

Solución:
    Se dividió el año en cuatrimestres:
        primer cuatrimestre de: 2017-01-01 a 2017-04-30
        segundo cuatrimestre de: 2017-05-01 a 2017-08-31
        tercer cuatrimestre de: 2017-09-01 a 2017-12-31

    Cada periodo es una llamada a la API por lo que en total en tres llamadas
    se obtiene el total de clientes creados en 2017

    Cada llamda regresa un objeto json con los datos de los clientes de ese
    cuatrimestre, por lo tanto se construyó un listado con cada elemento de la
    respuesta de cada una de las llamadas a la API
"""

import os
import requests

# Se importa el endpoint definido en el archivo .env
# La cual se exportó como variable de entorno
endpoint = os.environ.get('APIURL')

# Se divide el año en cuatrimestres
anio_dividido_en_cuatrimestres = {
    'primer_cuatrimestre': {
        'start': '2017-01-01',
        'end': '2017-04-30'
    },
    'segundo_cuatrimestre': {
        'start': '2017-05-01',
        'end': '2017-08-31'
    },
    'tercer_cuatrimestre': {
        'start': '2017-09-01',
        'end': '2017-12-31'
    }
}


def get_total_users():
    u"""
    Devuelve un listado de los clientes creados en 2017 en formato json.

    Endpoint:
        endpoint/users/:start/:end
        :start debe ser una fecha en formato YYYY-MM-DD
        :end debe ser una fecha en formato YYYY-MM-DD
    """
    # lista de todos los clientes vacia
    all_client_list = []

    for periodo, fecha in anio_dividido_en_cuatrimestres.items():
        # por cada periodo se obtienen la fecha inicial y final
        response = requests.get(
            # se pasan las fechas al endpoint como parametros
            endpoint+'/users/'+fecha['start']+'/'+fecha['end']
            # se obtiene la respuesta en formato json
        ).json()

        for item in response:
            # por cada elemento (cliente) en la respuesta
            # se agregan al listado total
            all_client_list.append(item)

    # se regresa el listado de todos los clientes
    return all_client_list
