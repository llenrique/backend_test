"""
Match the users and movementsself and create summaries.

The clients_summary function retrives a list of users and a list of movements.
Then iterates over each users to find the 'uid' and iterates over the movements
list to find the 'account' when those values are equals. Then acumulates the
values 'credit' and 'debit' for each user and increments the variable
movements_counter_by_user. Finally return a list that contains a summary for
each client.


create_summary function creates a required structure for the post endpoint. It
retrives the list of the function clients_summary and a general_summary created
in main file. Finally calls the function for send the result.

post_resume functio try to make a post request to the api_service and print the
response

"""

import json
from service import api_service


def clients_summary(users, movements):
    all_clients_summary = []
    for user in users:
        client_debit_sumary = 0
        client_credit_sumary = 0
        movements_counter_by_user = 0

        for move in movements:
            if move['account'] == user['uid']:
                movements_counter_by_user += 1
                if move['type'] == 'debit':
                    client_debit_sumary += move['amount']
                if move['type'] == 'credit':
                    client_credit_sumary += move['amount']

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


def create_summary(clients_summary, general_summary):
    print('Generando resumenes con estructua deseada')
    summary = {
        'totalRecords': general_summary['total_movements'],
        'totalCredit': general_summary['total_credit'],
        'totalDebit': general_summary['total_debit'],
        'balance': general_summary['balance'],
        'byUser': clients_summary
    }
    post_resume(summary)


def post_resume(resume):
    success = api_service.service_request('POST', 'conta/resumen', json=resume)
    print(success)
