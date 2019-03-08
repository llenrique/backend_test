from unittest import TestCase
from unittest.mock import patch, Mock
from service import api_service


class TestService(TestCase):
    @patch('service.api_service.requests.get')
    def test_service_on_user_success(self, mock_get):
        uri = 'users/2017-01-01/2017-01-04'

        users_mock = mock_get()

        users_mock.return_value.status_code = 200

        response = api_service.service_request('GET', uri)

        self.assertEqual(response.status_code, 200)

    @patch('service.api_service.requests.get')
    def test_service_on_user_fail(self, mock_get):
        uri = 'users/2017-01-01/2017-12-31'

        users_mock = mock_get()

        users_mock.return_value = 406

        response = api_service.service_request('GET', uri)

        self.assertEqual(response, 406)

    @patch('service.api_service.requests.get')
    def test_service_on_movements_fail(self, mock_get):
        uri = 'users/2017-01-01/2017-12-31'

        users_mock = mock_get()

        users_mock.return_value = 406

        response = api_service.service_request('GET', uri)

        self.assertEqual(response, 406)

    @patch('service.api_service.requests.get')
    def test_service_on_movements_success(self, mock_get):
        uri = 'users/2017-01-01/2017-01-13'

        users_mock = mock_get()

        users_mock.return_value.status_code = 200

        response = api_service.service_request('GET', uri)

        self.assertEqual(response.status_code, 200)
