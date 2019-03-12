from unittest import TestCase
from unittest.mock import patch
from performers import getters
from datetime import datetime


class TestGetters(TestCase):
    """docstring for TestGetters."""
    @patch('performers.getters.period_divisor')
    def test_get_users(self, mock_get_users):
        mock_get_users.return_value = 'Hay más de 50 resultados'
        start_date = datetime.strptime('2017-01-01', '%Y-%m-%d')
        end_date = datetime.strptime('2017-12-31', '%Y-%m-%d')
        users = getters.get_users(start_date.date(), end_date.date())

        self.assertEqual(users, "Hay más de 50 resultados")

    @patch('performers.getters.period_divisor')
    def test_get_movements(self, mock_get_movements):
        mock_get_movements.return_value = 'Hay más de 50 resultados'
        start_date = datetime.strptime('2018-01-01', '%Y-%m-%d')
        end_date = datetime.strptime('2018-12-31', '%Y-%m-%d')
        movements = getters.get_movements(start_date.date(), end_date.date())

        self.assertEqual(movements, "Hay más de 50 resultados")
