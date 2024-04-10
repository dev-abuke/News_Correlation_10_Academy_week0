import unittest
import os
from src.loader import NewsDataLoader

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.loader = NewsDataLoader('path_to_test_files')

    def test_get_news(self):
        expected_path = os.path.join('path_to_test_files', 'rating.csv')
        self.assertEqual(self.loader.get_news(), expected_path)

    def test_get_traffic(self):
        expected_path = os.path.join('path_to_test_files', 'traffic.csv')
        self.assertEqual(self.loader.get_traffic(), expected_path)

    def test_get_domain_location(self):
        expected_path = os.path.join('path_to_test_files', 'domains_location.csv')
        self.assertEqual(self.loader.get_domain_location(), expected_path)

if __name__ == '__main__':
    unittest.main()