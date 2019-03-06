import json
from service import service

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
    success = service.make_request('POST', 'conta/resumen', json=resume)
    print(success)
