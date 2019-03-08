"""Functions for get users or movements."""


from performers.periods import period_divisor


def get_users(start_date, end_date):
    """This function tells period_divisor get users in the period of time."""
    result = period_divisor(start_date, end_date, 'users')
    return result


def get_movements(start_date, end_date):
    """This function tells period_divisor get movements in the period of time"""
    result = period_divisor(start_date, end_date, 'movements')
    return result
