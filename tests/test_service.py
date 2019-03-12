from unittest import TestCase
from service import api_service
import requests_mock


class TestService(TestCase):
    @requests_mock.Mocker()
    def test_service_on_success(self, mock):
        user = [{'name': 'Enrique'}]

        mock.get(
            requests_mock.ANY,
            json=user,
            status_code=200
        )

        res = api_service.service_request('GET', 'users/2017-01-01/2017-01-14')

        self.assertEqual(res, user)

    @requests_mock.Mocker()
    def test_service_on_fail(self, mock):
        response = False

        mock.get(
            requests_mock.ANY,
            status_code=406
        )

        res = api_service.service_request('GET', 'users/2017-01-01/2017-12-31')

        self.assertEqual(res, response)
