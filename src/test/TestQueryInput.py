from src.python.QueryFormat import TABLEUPLOAD
from src.python.DataQueryGPT import QUERYCOMPLETION
import subprocess

def test_data_query(query) -> str:
    q_completion = QUERYCOMPLETION()
    q_completion.get_completion("This is a test completion. Return Response 200 if this completion is valid.")
    q_completion.get_completion(query)

def test_upload_data(id, query, completion, response_accepted, acceptance_target, environment, query_type, actual_response):
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
    t_upload.upload_data()


def test_upload_shell(id, query, completion, environment, query_type, response_accepted=True, acceptance_target=0.97, actual_response=None):
    subprocess.run(
        f'bash src/bash/table-population.sh {environment} {id} {query} {query_type} {completion} {response_accepted} {acceptance_target} {actual_response}',
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )