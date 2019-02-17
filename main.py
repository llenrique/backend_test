u"""
Examen de candidato para Resuelve tu deuda.

Autor: Enrique López
Email: llenriquelopez@gmail.com
Fecha: 14/Febrero/2019

Version: 0.0.1
"""

import movements
import clients
import summary
import os
import requests


def posts_results(resume):
    r = requests.post(os.environ.get('APIURL')+'/conta/resumen', json=resume)
    print(r.text)


if __name__ == '__main__':
    total_clients = clients.get_total_users()

    total_movements = movements.get_total_movements()

    total_debit = movements.get_total_for_type(total_movements, 'debit')
    total_credit = movements.get_total_for_type(total_movements, 'credit')
    balance = total_credit + total_debit

    general_summary = {
        'total_debit': total_debit,
        'total_credit': total_credit,
        'balance': balance,
        'total_movements': len(total_movements)
    }

    clients_summary = clients.clients_summary(total_clients, total_movements)

    resume = summary.create_summary(clients_summary, general_summary)

    posts_results(resume)
