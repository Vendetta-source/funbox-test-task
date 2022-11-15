"""
Юнит-тесты
"""

import unittest
from .views import LinksAPIView


class TestClearData(unittest.TestCase):

    def setUp(self):
        self.instance = LinksAPIView()
        self.data = ["https://ya.ru", "https://ya.ru?q=123", "funbox.ru",
                     "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
                     "http://google.com///",
                     "http://www.youtube.com/"]

    def test_clear_data(self):
        result = self.instance.clear_data(self.data)
        self.assertEqual(result, ['ya.ru', 'ya.ru', 'funbox.ru', 'stackoverflow.com', 'google.com', 'youtube.com'])

    def test_clear_data_zero_links(self):
        result = self.instance.clear_data([])
        self.assertEqual(result, [])