#Sofia Mase
import unittest
from news_focus import app

class TestNewsFocus(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_asu_topics(self):
        # Test the NewsFocus service with ASU topics
        topics = ["Tuition increase", "QS Ranking"]  # Add topics here
        response = self.app.get('/news', query_string={"topics[]": topics})
        data = response.get_json()

        # Assert that the response is as expected.
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tuition increase", data)
        self.assertTrue(isinstance(data["Tuition increase"], list))
        self.assertIn("QS Ranking", data)
        self.assertTrue(isinstance(data["QS Ranking"], list))

if __name__ == '__main__':
    unittest.main()
