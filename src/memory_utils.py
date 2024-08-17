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
    try:
        query_job = client.query(query)
        query_job.result()

        results = query_job.result()
        return results
    except Exception as e:
        print(f"An error ocurred: {e}")
        return None