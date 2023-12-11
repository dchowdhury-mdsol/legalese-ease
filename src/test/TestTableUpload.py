import unittest
from unittest.mock import patch
from src.python.QueryFormat import TABLEUPLOAD

class TestTableUpload(unittest.TestCase):
    """
    Test suite for the TABLEUPLOAD class in the QueryFormat module.

    This class contains unit tests for testing the functionality of TABLEUPLOAD,
    including the proper formatting of data for DynamoDB and the upload process.
    """

    def test_json_format(self):
        """
        Test case for the JSON formatting functionality in TABLEUPLOAD.

        Ensures that data is correctly formatted into the structure required by DynamoDB.
        """
        # Example data to be formatted
        test_data = {
            'id': 123,
            'query': 'Test Query',
            'completion': 'Test Completion',
            'response_accepted': True,
            'acceptance_target': 0.95,
            'environment': 'test',
            'query_type': 'Test Type',
            'actual_response': 'Test Response'
        }

        # Create an instance of TABLEUPLOAD with the test data
        table_upload = TABLEUPLOAD(**test_data)

        # Get the JSON-formatted data
        json_data = table_upload._TABLEUPLOAD__json_format()  # Accessing the private method

        # Assert the structure and content of the JSON-formatted data
        self.assertEqual(json_data['TableName'], f"legalese-ease-{test_data['environment']}")
        self.assertIn('Item', json_data)

        # Assert each field in 'Item'
        self.assertEqual(json_data['Item']['ID']['N'], str(test_data['id']))
        self.assertEqual(json_data['Item']['Query']['S'], test_data['query'])
        self.assertEqual(json_data['Item']['QueryResponse']['S'], test_data['completion'])
        self.assertEqual(json_data['Item']['ResponseAccepted']['BOOL'], test_data['response_accepted'])
        self.assertEqual(json_data['Item']['ResponseAcceptanceTarget']['N'], str(test_data['acceptance_target']))
        self.assertEqual(json_data['Item']['QueryType']['S'], test_data['query_type'] if test_data['query_type'] else 'None')
        self.assertEqual(json_data['Item']['AcceptedResponse']['S'], test_data['actual_response'] if test_data['actual_response'] else 'None')

    @patch('QueryFormat.boto3.client')
    def test_upload_data(self, mock_boto_client):
        """
        Test case for the data upload functionality in TABLEUPLOAD.

        This test verifies that the TABLEUPLOAD class can successfully call the
        DynamoDB PutItem operation. DynamoDB interactions are mocked.
        """
        # Example data for upload
        test_data = {
            'id': 123,
            'query': 'Test Query',
            'completion': 'Test Completion',
            'response_accepted': True,
            'acceptance_target': 0.95,
            'environment': 'test',
            'query_type': 'Test Type',
            'actual_response': 'Test Response'
        }

        # Mock the DynamoDB client
        mock_dynamodb = mock_boto_client.return_value

        # Create an instance of TABLEUPLOAD and call upload_data
        table_upload = TABLEUPLOAD(**test_data)
        table_upload.upload_data()

        # Verify that the DynamoDB client was called with expected parameters
        mock_dynamodb.put_item.assert_called_once()
        # Extract the call arguments to assert the structure and content
        called_args = mock_dynamodb.put_item.call_args[1]
        self.assertEqual(called_args['TableName'], f"legalese-ease-{test_data['environment']}")
        self.assertIn('Item', called_args)

        # Assert each field in 'Item' based on the call arguments
        item_args = called_args['Item']
        self.assertEqual(item_args['ID']['N'], str(test_data['id']))
        self.assertEqual(item_args['Query']['S'], test_data['query'])
        self.assertEqual(item_args['QueryResponse']['S'], test_data['completion'])
        self.assertEqual(item_args['ResponseAccepted']['BOOL'], test_data['response_accepted'])
        self.assertEqual(item_args['ResponseAcceptanceTarget']['N'], str(test_data['acceptance_target']))
        self.assertEqual(item_args['QueryType']['S'], test_data['query_type'] if test_data['query_type'] else 'None')
        self.assertEqual(item_args['AcceptedResponse']['S'], test_data['actual_response'] if test_data['actual_response'] else 'None')

if __name__ == '__main__':
    unittest.main()