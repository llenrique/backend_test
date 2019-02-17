u""".

Problema:
    Obtener un listado de todos los movimientos generales creados en 2018
    Las fechas deben estarn en formato YYYY-MM-DD

Descripción:
    Trae un listado de los movimientos que fueron creados entre las fechas
    de inicio y fin

    Las fechas deben estar en formato YYYY-MM-DD

    Si hay más de 50 registros en el rango de fechas, contesta con la leyenda:
    "Hay más de 50 resultados" y el status 406
"""

import os
import requests

endpoint = os.environ.get('APIURL')

periodos = {
    # 'primer': {
    #     'start': '2018-01-01',
    #     'end': '2018-01-13'
    # },
    # 'segundo': {
    #     'start': '2018-01-14',
    #     'end': '2018-01-21'
    # },
    # 'tercer': {
    #     'start': '2018-01-22',
    #     'end': '2018-02-01'
    # },
    # 'cuarto': {
    #     'start': '2018-02-02',
    #     'end': '2018-02-13'
    # },
    # 'quinto': {
    #     'start': '2018-02-14',
    #     'end': '2018-02-21'
    # },
    # 'secxto': {
    #     'start': '2018-02-22',
    #     'end': '2018-03-03'
    # },
    # 'septimo': {
    #     'start': '2018-03-04',
    #     'end': '2018-03-14'
    # },
    # 'octavo': {
    #     'start': '2018-03-15',
    #     'end': '2018-03-26'
    # },
    # 'noveno': {
    #     'start': '2018-03-27',
    #     'end': '2018-04-05'
    # },
    # 'decimo': {
    #     'start': '2018-04-06',
    #     'end': '2018-04-13'
    # },
    # 'decimo_primero': {
    #     'start': '2018-04-14',
    #     'end': '2018-04-23'
    # },
    # 'decimo_segundo': {
    #     'start': '2018-04-24',
    #     'end': '2018-05-05'
    # },
    # 'decimo_tecero': {
    #     'start': '2018-05-06',
    #     'end': '2018-05-15'
    # },
    # 'decimo_cuarto': {
    #     'start': '2018-05-16',
    #     'end': '2018-05-25',
    # },
    # 'decimo_quinto': {
    #     'start': '2018-05-26',
    #     'end': '2018-06-06',
    # },
    # 'decimo_sexto': {
    #     'start': '2018-06-07',
    #     'end': '2018-06-18',
    # },
    # 'decimo_septimo': {
    #     'start': '2018-06-18',
    #     'end': '2018-06-27',
    # },
    # 'decimo_octavo': {
    #     'start': '2018-06-28',
    #     'end': '2018-07-05',
    # },
    # 'decimo_noveno': {
    #     'start': '2018-07-06',
    #     'end': '2018-07-16',
    # },
    # 'vigesimo': {
    #     'start': '2018-07-17',
    #     'end': '2018-07-26',
    # },
    # 'vigesimo_primero': {
    #     'start': '2018-07-27',
    #     'end': '2018-08-06',
    # },
    # 'vigesimo_segundo': {
    #     'start': '2018-08-07',
    #     'end': '2018-08-16',
    # },
    # 'vigesimo_tercero': {
    #     'start': '2018-08-17',
    #     'end': '2018-08-27',
    # },
    # 'vigesimo_cuarto': {
    #     'start': '2018-08-28',
    #     'end': '2018-09-04',
    # },
    # 'vigesimo_quinto': {
    #     'start': '2018-09-05',
    #     'end': '2018-09-12',
    # },
    # 'vigesimo_sexto': {
    #     'start': '2018-09-13',
    #     'end': '2018-09-21',
    # },
    # 'vigesimo_septimo': {
    #     'start': '2018-09-22',
    #     'end': '2018-10-04',
    # },
    # 'vigesimo_octavo': {
    #     'start': '2018-10-05',
    #     'end': '2018-10-16',
    # },
    # 'vigesimo_noveno': {
    #     'start': '2018-10-16',
    #     'end': '2018-10-24',
    # },
    'trigesimo': {
        'start': '2018-10-25',
        'end': '2018-11-03',
    },
    'trigesimo_primero': {
        'start': '2018-11-04',
        'end': '2018-12-31',
    }
}


def get_total_movements():
    u"""
    Esta función obtiene los movimientos realizados por los clientes en 2018.


    """
    print('Obteniendo movimientos')
    all_movements_list = []

    for periodo, fecha in periodos.items():
        response = requests.get(
            endpoint+'/movements/'+fecha['start']+'/'+fecha['end']
        ).json()

        # print('periodo {} : {} movimientos'.format(periodo, len(response)))

        for item in response:
            all_movements_list.append(item)

    print('Número de movimientos {}'.format(len(all_movements_list)))

    return all_movements_list


def get_total_for_type(movements, type):
    print('Calculando total de {}'.format(type))
    total = 0
    for item in movements:
        if(item['type'] == type):
            total += item['amount']
    print('{} total: {}'.format(type, total))
    return total
