u"""Get the amount for CREDIT and DEBIT.

In a movements list it iterates over each item and check the value "type" to
determinate if it is 'debit' or 'credit' and acumulate the value of each case
in specific variables


Example:
    For each item on movements list:
        If the 'type' of current item is debit:
            acumulate it on total_debit variable
        If the 'type' of current item is credit:
            acumulate it on total_credit variable

    return both variables
"""


def get_total_amounts(movements):
    total_debit = 0
    total_credit = 0
    for item in movements:
        if item['type'] == 'debit':
            total_debit += item['amount']
        elif item['type'] == 'credit':
            total_credit += item['amount']
    totals = [total_debit, total_credit]
    return totals
