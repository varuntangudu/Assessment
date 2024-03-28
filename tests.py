import unittest
from server import app
import json

class TestWeatherEndpoints(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_weather_records(self):
        # Test with valid query parameters
        response = self.app.get('/api/weather?date=1985-01-01&station_id=USC00110072&page=0')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        if not data:
            self.fail("NO data found with the given weather parameters")

        # Test with missing query parameters
        response = self.app.get('/api/weather')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        if not data:
            self.assertEqual(response.data.decode(), "No valid Weather data")

    def test_get_weather_stats(self):
        # Test with valid query parameters
        response = self.app.get('/api/weather/stats?date=1985-01-01&station_id=USC00110072&page=0')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        if not data:
            self.fail("NO data found with the given stats parameters")

        # Test with missing query parameters
        response = self.app.get('/api/weather/stats')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        if not data:
            self.assertEqual(response.data.decode(), "No Valid Station Data")

if __name__ == '__main__':
    unittest.main()
