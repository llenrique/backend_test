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

    Parametros:
        :start debe ser una fecha en formato YYYY-MM-DD
        :end debe ser una fecha en formato YYYY-MM-DD

    Response:
        La API regresa un objeto JSON que contiene a cada usuario con la
        siguiente información:
            el nombre de cada cliente
            su primer y segundo apellido
            el uid del cliente
            su correo electrónico
            su status (active, false o true)
            su fecha de creación
    """
    # lista de todos los clientes vacia
    all_client_list = []

    print('Obteniendo lista de clientes')
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

    print('Número de clientes {}'.format(len(all_client_list)))

    # se regresa el listado de todos los clientes
    return all_client_list


def clients_summary(users, movements):
    u"""Esta función genera el resumen de cada cliente."""
    print('Relacionando clientes con movimientos, generando resumen')
    print('...Calculando total de movimientos por cliente')
    print('...Calculando credit total por cliente')
    print('...Calculando debit total por cliente')
    print('...Calculando balance por cliente')
    all_clients_summary = []
    for user in users:
        client_debit_sumary = 0
        client_credit_sumary = 0
        movements_counter_by_user = 0

        for move in movements:
            if move['account'] == user['uid'] and move['amount'] != 0:
                movements_counter_by_user += 1
                if move['type'] == 'debit':
                    client_debit_sumary += move['amount']
                elif move['type'] == 'credit':
                    client_credit_sumary += move['amount']

                movements.remove(move)

            clients_summary = {
                'nombre': user['nombre'],
                'uid': user['uid'],
                'records': movements_counter_by_user,
                'resumen': {
                    'credit': client_credit_sumary,
                    'debit': client_debit_sumary,
                    'balance': client_credit_sumary - client_debit_sumary
                }
            }

        all_clients_summary.append(clients_summary)
    return all_clients_summary
