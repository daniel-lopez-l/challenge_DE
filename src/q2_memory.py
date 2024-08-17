from typing import List, Tuple
from google.cloud import bigquery
from memory_profiler import profile
from memory_utils import execute_query_for_memory

@profile
def q2_memory(client: bigquery.Client, query: str) ->  List[Tuple[str, int]]:

    results = execute_query_for_memory(client, query)

    output = [(row.emoji, row.total_emoji) for row in results]

    return output
