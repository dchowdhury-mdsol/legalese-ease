import unittest
from unittest.mock import patch
from src.python.DataQueryGPT import QUERYCOMPLETION

class TestQueryCompletion(unittest.TestCase):
    """
    Test suite for the QUERYCOMPLETION class in the DataQueryGPT module.

    This class contains unit tests for testing the functionality of QUERYCOMPLETION,
    including initialization and its method for getting AI completions.
    """

    def test_init(self):
        """
        Test case for the initialization of QUERYCOMPLETION.

        Ensures that the API_KEY provided during initialization is correctly set.
        """
        # Initialize QUERYCOMPLETION with a dummy API key
        query = QUERYCOMPLETION("dummy_api_key")

        # Assert that the API_KEY is set correctly
        self.assertEqual(query.API_KEY, "dummy_api_key")

    @patch('DataQueryGPT.openai.ChatCompletion.create')
    def test_get_completion(self, mock_openai):
        """
        Test case for the get_completion method in QUERYCOMPLETION.

        This test verifies that the method correctly calls the OpenAI API and processes the response.
        The OpenAI API call is mocked to avoid network calls and potential costs during testing.
        """
        # Mock response from the OpenAI API
        mock_response = {
            'choices': [{
                'message': {'content': "Test completion"}
            }]
        }
        mock_openai.return_value = mock_response

        # Initialize QUERYCOMPLETION with a dummy API key
        query = QUERYCOMPLETION("dummy_api_key")

        # Define a test prompt
        prompt = "Test prompt"

        # Call the get_completion method and capture the output
        completion = query.get_completion(prompt)

        # Verify that the OpenAI API call was made with expected parameters
        mock_openai.assert_called_with(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}], temperature=0)

        # Assert that the method returns the expected mock response
        self.assertEqual(completion, "Test completion")

if __name__ == '__main__':
    unittest.main()