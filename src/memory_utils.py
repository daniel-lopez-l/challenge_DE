from typing import Any
from google.cloud import bigquery

def execute_query_for_memory(client: bigquery.Client, query:str) -> Any:
    """
    Execute and return the result of query
    Args:
        client (bigquery.Client),
        query (str)
    Returns: 
        result of query
    """
    query_job = client.query(query)
    query_job.result()

    results = query_job.result()
    return results