import json
import argparse
import boto3
from SetupLogger import setup_logging

# Create a class for dynamoDB table population
class TABLEUPLOAD():
    def __init__(self, id:int, query:str, completion:str, response_accepted:bool, acceptance_target:float, environment:str, query_type:None, actual_response=None) -> str:
        """
        Constructor for TABLEUPLOAD class.

        Parameters:
        - id (int): ID value of the object in the target table.
        - query (str): Original query from the user.
        - completion (str): Original response from GPT AI.
        - response_accepted (bool): Is the completion response accepted? [True/False]
        - acceptance_target (float): Percent target of acceptance for completion response.
        - query_type (str, optional): Type of legal query.
        - actual_response (str, optional): Actual expected response if the completion response is unaccepted.
        - environment (str): Development environment.

        Returns:
        - str: JSON-formatted data to upload to DynamoDB.
        """
        # Initialize class attributes
        self.id = id
        self.query = query
        self.completion = completion
        self.response_accepted = response_accepted
        self.acceptance_target = acceptance_target
        self.query_type = query_type
        self.actual_response = self.completion if self.response_accepted else actual_response
        self.environment = environment
    
    def __json_format(self) -> json:
        """
        Private method to format data as JSON.

        Returns:
        - str: JSON-formatted data.
        """
        # Create a dictionary with the required structure for DynamoDB
        data = {
            "TableName": f"legalese-ease-{self.environment}",
            "Item": {
                "ID": {"N": str(self.id)},  # Assuming ID is a number attribute
                "QueryType": {"S": self.query_type},
                "Query": {"S": self.query},
                "QueryResponse": {"S": self.completion},
                "ResponseAccepted": {"BOOL": self.response_accepted},
                "ResponseAcceptanceTarget": {"N": str(self.acceptance_target)},
                "AcceptedResponse": {"S": self.actual_response}
            }
        }
        
        # Convert the dictionary to a JSON string with indentation
        return json.dumps(data, indent=4)
    
    def upload_data(self) -> dict:
        """
        Method to upload data to DynamoDB using Boto3.

        Returns:
        - dict: Response from the DynamoDB PutItem operation.
        """
        # Create a Boto3 DynamoDB client
        dynamodb = boto3.client('dynamodb')  # Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
        
        # Format data as JSON
        data = self.__json_format()
        
        # Use the PutItem operation to upload the data to the DynamoDB table
        return dynamodb.put_item(
            TableName = f'legalese-ease-{self.environment}',
            Item = data["Item"]
        )
    
if __name__ == "__main__":
    # Create an argument parser to get input values from the command line
    parser = argparse.ArgumentParser(description="Get accepted JSON formatted response to prepare upload to DynamoDB.")
    
    # Define command-line arguments
    parser.add_argument("ID", type=str, help="ID value of object in target table.")
    parser.add_argument("QUERY", type=str, help="Original query from the user.")
    parser.add_argument("COMPLETION", type=str, help="Original response from GPT AI.")
    parser.add_argument("RESPONSE_ACCEPTED", type=bool, help="Is the completion response accepted? [True/False]")
    parser.add_argument("ACCEPTANCE_TARGET", type=float, help="Percent target of acceptance for completion response.")
    parser.add_argument("QUERY_TYPE", type=str, default=None, help="Type of legal query.")
    parser.add_argument("ACTUAL_RESPONSE", type=str, default=None, help="Actual expected response if the completion response is unaccepted.")
    parser.add_argument("ENVIRONMENT", type=str, help="Development environment.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Create an instance of the TABLEUPLOAD class
    table_upload = TABLEUPLOAD(
        id=args.ID, 
        query=args.QUERY, 
        completion=args.COMPLETION, 
        response_accepted=args.RESPONSE_ACCEPTED, 
        acceptance_target=args.ACCEPTANCE_TARGET,
        query_type=args.QUERY_TYPE,
        actual_response=args.ACTUAL_RESPONSE,
        environment=args.ENVIRONMENT
    )

    # Set up logging and obtain a logger instance
    logger = setup_logging()  # Assuming you have a function 'setup_logging' for configuring logging

    # Upload data to DynamoDB
    response = table_upload.upload_data()

    # Log the response from DynamoDB
    logger.info("DynamoDB Response: %s", response)

