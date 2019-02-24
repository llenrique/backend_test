u"""
Examen de candidato backend de Resuelve tu deuda.

Autor: Enrique López
Email: llenriquelopez@gmail.com
Fecha: 14/Febrero/2019

Version: 0.1.0
"""

from my_requests import get_total, posts_results
from amounts import get_total_amounts
from summary import clients_summary, create_summary
from periodos import clientes, movimientos


if __name__ == '__main__':
    total_clients = get_total(clientes, 'users')
    total_movements = get_total(movimientos, 'movements')

    totals = get_total_amounts(total_movements)

    balance = totals[1] + totals[0]

    general_summary = {
        'total_debit': totals[0],
        'total_credit': totals[1],
        'balance': balance,
        'total_movements': len(total_movements)
    }

    clients_summary = clients_summary(total_clients, total_movements)

    resume = create_summary(clients_summary, general_summary)

    # posts_results(resume)
