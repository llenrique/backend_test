u"""
Examen de candidato backend de Resuelve tu deuda.

Autor: Enrique López
Email: llenriquelopez@gmail.com
Fecha: 14/Febrero/2019

Version: 0.1.0
"""

from getters import get_users, get_movements
from dates_manager import set_date
from amounts import get_total_amounts
from summary import summary


if __name__ == '__main__':
    start_date = set_date('start')
    end_date = set_date('end')

    users = get_users(start_date, end_date)

    print('Users found: {}'.format(len(users)))

    start_date = set_date('start')
    end_date = set_date('end')

    movements = get_movements(start_date, end_date)

    print('Movements found: {}'.format(len(movements)))

    users = summary.clients_summary(users, movements)

    total_credit, total_debit = get_total_amounts(movements)

    balance = total_credit - total_debit

    general_summary = {
        'total_debit': total_debit,
        'total_credit': total_credit,
        'balance': balance,
        'total_movements': len(movements)
    }

    resume = summary.create_summary(users, general_summary)
