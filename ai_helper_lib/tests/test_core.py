import unittest
from ai_helper.core import get_response, summarize_text, format_response

class TestAIHelper(unittest.TestCase):
    def test_get_response(self):
        prompt = "Hello"
        response = get_response(prompt)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_summarize_text(self):
        short_text = "Short text"
        self.assertEqual(summarize_text(short_text), short_text)
        
        long_text = "A" * 60
        summary = summarize_text(long_text)
        self.assertTrue(summary.endswith("(summarized)"))
        self.assertTrue(len(summary) < 70)

    def test_format_response(self):
        raw = "  hello world  "
        formatted = format_response(raw)
        self.assertEqual(formatted, "Hello world")

if __name__ == '__main__':
    unittest.main()
