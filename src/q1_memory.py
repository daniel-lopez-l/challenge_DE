from typing import List, Tuple
from google.cloud import bigquery

from memory_profiler import profile

@profile
def q1_memory(client: bigquery.Client, query: str) ->  List[Tuple[str, str]]:

    query_job = client.query(query)
    query_job.result()

    results = query_job.result()

    output = [(row.top_user, row.date) for row in results]

    return output
