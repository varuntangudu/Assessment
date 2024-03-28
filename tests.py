import unittest
from server import app

class TestWeatherEndpoints(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_weather_records(self):
        # Test with valid query parameters
        response = self.app.get('/api/weather?date=2024-03-27&station_id=123&page=1')
        self.assertEqual(response.status_code, 200)

        # Test with missing query parameters
        response = self.app.get('/api/weather')
        self.assertEqual(response.status_code, 200)

    def test_get_weather_stats(self):
        # Test with valid query parameters
        response = self.app.get('/api/weather/stats?date=2024-03-27&station_id=123&page=1')
        self.assertEqual(response.status_code, 200)

        # Test with missing query parameters
        response = self.app.get('/api/weather/stats')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
