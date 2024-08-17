from typing import Any
from google.cloud import bigquery

def execute_query_for_memory(client: bigquery.Client, query:str) -> Any:
    query_job = client.query(query)
    query_job.result()

    results = query_job.result()
    
    return results