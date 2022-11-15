"""
Интеграционные тесты
"""
import json
import time

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class APITest(APITestCase):

    def setUp(self):
        self.test_links1 = {"links": ["https://ya.ru", "https://ya.ru?q=123", "funbox.ru",
                                      "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"]}
        self.test_links2 = {"links": ["https://ya.ru", "https://google.com?q=293848934", "funbox.ru",
                                      "https://hh.ru/", "https://www.linkedin.com/in/tamerlan-kabulov/"]}

    def test_error_add_links(self):
        response = self.client.post('/api/v1/visited_links/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"status": "error"})

    def test_add_links(self):
        response = self.client.post('/api/v1/visited_links/', self.test_links1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_add_links_and_get_links(self):
        self.client.post('/api/v1/visited_links/', self.test_links1, content_type='application/json')
        from_time = round(time.time())
        time.sleep(5)
        self.client.post('/api/v1/visited_links/', self.test_links2, content_type='application/json')
        to_time = round(time.time())

        response = self.client.get(f'/api/v1/visited_domains/?from={from_time - 10}&to={to_time + 10}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"domains": ['funbox.ru',
                                                       'google.com',
                                                       'hh.ru',
                                                       'linkedin.com',
                                                       'stackoverflow.com',
                                                       'ya.ru',
                                                       ],
                                           "status": "ok"})
