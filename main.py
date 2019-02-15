u"""
Examen de candidato para Resuelve tu deuda.

Autor: Enrique López
Email: llenriquelopez@gmail.com
Fecha: 14/Febrero/2019

Version: 0.0.1
"""

from all_clients_list import get_total_users


if __name__ == '__main__':
    result = get_total_users()

    print(len(result))
