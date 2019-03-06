from periods import period_divisor


def get_users(start_date, end_date):
    result = period_divisor(start_date, end_date, 'users')
    return result


def get_movements(start_date, end_date):
    result = period_divisor(start_date, end_date, 'movements')
    return result
