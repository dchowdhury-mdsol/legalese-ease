from src.python.QueryFormat import TABLEUPLOAD
from src.python.DataQueryGPT import QUERYCOMPLETION
import subprocess

def test_data_query(query) -> str:
    """
    Test function for querying data using the QUERYCOMPLETION class.

    This function simulates the process of fetching a completion for a given query
    using the QUERYCOMPLETION class from the DataQueryGPT module.

    Parameters:
    - query (str): The query string to be sent to the QUERYCOMPLETION class for completion.

    Returns:
    - str: The response from the QUERYCOMPLETION.get_completion method.
    """
    # Create an instance of QUERYCOMPLETION
    q_completion = QUERYCOMPLETION()

    # Fetch completion for a test statement
    q_completion.get_completion("This is a test completion. Return Response 200 if this completion is valid.")

    # Fetch completion for the actual query provided as a parameter
    return q_completion.get_completion(query)

def test_upload_data(id, query, completion, response_accepted, acceptance_target, environment, query_type, actual_response):
    """
    Test function for uploading data using the TABLEUPLOAD class.

    This function simulates the process of uploading data to a database (or similar storage)
    using the TABLEUPLOAD class from the QueryFormat module.

    Parameters:
    - id (int): The ID value for the data entry.
    - query (str): The original query string.
    - completion (str): The AI-generated completion string.
    - response_accepted (bool): Indicates if the completion response is accepted.
    - acceptance_target (float): The acceptance target percentage.
    - environment (str): The development or production environment.
    - query_type (str): The type of query.
    - actual_response (str): The actual expected response if the completion is not accepted.
    """
    # Create an instance of TABLEUPLOAD with provided parameters
    t_upload = TABLEUPLOAD(
        id=id,
        query=query,
        completion=completion,
        response_accepted=response_accepted,
        acceptance_target=acceptance_target,
        environment=environment,
        query_type=query_type,
        actual_response=actual_response
    )

    # Upload data using the TABLEUPLOAD instance
    t_upload.upload_data()

def test_upload_shell(id, query, completion, environment, query_type, response_accepted=True, acceptance_target=0.97, actual_response=None):
    """
    Test function for uploading data using a shell script.

    This function simulates the process of uploading data by invoking a bash script.
    It uses the subprocess module to run the script with necessary arguments.

    Parameters:
    - id (int): The ID value for the data entry.
    - query (str): The original query string.
    - completion (str): The AI-generated completion string.
    - environment (str): The development or production environment.
    - query_type (str): The type of query.
    - response_accepted (bool): Indicates if the completion response is accepted.
    - acceptance_target (float): The acceptance target percentage.
    - actual_response (str): The actual expected response if the completion is not accepted.
    """
    # Run a bash script with the provided arguments
    subprocess.run(
        f'bash src/bash/table-population.sh {environment} {id} {query} {query_type} {completion} {response_accepted} {acceptance_target} {actual_response}',
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )