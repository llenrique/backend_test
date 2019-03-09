u"""
Examen de candidato backend de Resuelve tu deuda.

Autor: Enrique López
Email: llenriquelopez@gmail.com
Fecha: 14/Febrero/2019

Version: 0.1.0
"""

from performers.getters import get_users, get_movements
from performers.dates_manager import set_date
from summary.amounts import get_total_amounts
from summary import summary


if __name__ == '__main__':
    print('====GET USERS====')
    users = get_users(set_date('start'), set_date('end'))

    print('Users found: {}'.format(len(users)))

    print('====GET MOVEMENTS====')
    movements = get_movements(set_date('start'), set_date('end'))

    print('Movements found: {}'.format(len(movements)))

    users = summary.clients_summary(users, movements)

    total_debit, total_credit = get_total_amounts(movements)

    balance = total_credit - total_debit

    general_summary = {
        'total_debit': total_debit,
        'total_credit': total_credit,
        'balance': balance,
        'total_movements': len(movements)
    }

    resume = summary.create_summary(users, general_summary)
