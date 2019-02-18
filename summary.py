import json
import requests


def create_summary(clients_summary, general_summary):
    print('Generando resumenes con estructua deseada')
    summary = {
        'totalRecords': general_summary['total_movements'],
        'totalCredit': general_summary['total_credit'],
        'totalDebit': general_summary['total_debit'],
        'balance': general_summary['balance'],
        'byUser': clients_summary
    }
    print('Generando archivo de salida balance.json')
    with open('balance.json', 'w') as outfile:
        json.dump(summary, outfile, indent=2)

    return summary
