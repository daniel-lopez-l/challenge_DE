from typing import List, Tuple
from google.cloud import bigquery

from memory_profiler import profile

@profile
def q1_memory(client: bigquery.Client, query: str) ->  List[Tuple[str, str]]:
<<<<<<< HEAD
    """
    Execute and return the result of query and the memory
    Args:
        client (bigquery.Client),
        query (str)
    Returns: 
        result of query
    """
    results = execute_query_for_memory(client, query)
=======

    query_job = client.query(query)
    query_job.result()

    results = query_job.result()
>>>>>>> main

    output = [(row.top_user, row.date) for row in results]

    return output
