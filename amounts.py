u"""Obtención del valor total de CREDIT y DEBIT.

En una lista de los movimientos se itera sobre cada item evaluando el valor
'type' para determinar si es 'debit' o 'credit' y acumular el valor de la
propiedad 'amount' en variables especificas.


TODO:
    Para cada elemento en la lista de movimientos:
        Si el 'type' del movimiento actual es 'debit'
            el monto se acumula en la variable 'total_debit'
        Si el 'type' es 'credit':
            el monto se acumla en la variable 'total_credit'
        Se regresan ambas variables
"""


def get_total_amounts(movements):
    u"""
    Acumula el total de credit y debit y devuelve estos valores.

    Parametros:
        movements: lista de diccionarios que describe la infrormación de cada
        movimiento

    Return:
        Array: Con los totales de credit y debit
    """
    total_debit = 0
    total_credit = 0
    for item in movements:
        if item['type'] == 'debit':
            total_debit += item['amount']
        elif item['type'] == 'credit':
            total_credit += item['amount']
    totals = [total_debit, total_credit]
    return totals