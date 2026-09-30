import unittest
from src.features import extract, predict, risk_score

class FeatureTests(unittest.TestCase):
    def test_ip_and_at_symbol_are_signals(self):
        features = extract("http://192.0.2.10/login@evil.example")
        self.assertEqual(features["has_ip"], 1.0)
        self.assertEqual(features["at_symbol"], 1.0)

    def test_benign_example_stays_low(self):
        self.assertEqual(predict("https://www.example.com/about"), 0)

    def test_suspicious_example_scores_high(self):
        self.assertGreaterEqual(risk_score("http://192.0.2.10/login"), 3)
        self.assertEqual(predict("http://192.0.2.10/login"), 1)

if __name__ == "__main__":
    unittest.main()
