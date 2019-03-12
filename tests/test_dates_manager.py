from unittest import TestCase
from unittest.mock import patch
from datetime import datetime
from performers import dates_manager


class TestSetDate(TestCase):
    @patch('performers.dates_manager.input', return_value='2017-01-01')
    def test_set_date(self, mock_set_date):
        date = datetime.strptime('2017-01-01', '%Y-%m-%d')
        self.assertEqual(dates_manager.set_date('start'), date.date())
