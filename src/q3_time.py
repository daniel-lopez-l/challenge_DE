from typing import List, Tuple
from time_utils import execute_time_query
from google.cloud import bigquery


def q3_time(client: bigquery.Client, query: str) -> Tuple[List[Tuple[str, int]], float]:
    """
    Execute exetute_time_query functions for return the result of query and time
    Args:
        client (bigquery.Client),
        query (str)
    Returns: 
        result of query and the time in ms
    """
    q3_query_result, q2_time_result  = execute_time_query(client ,query)
    output = [(row.top_mentioned, row.total_mencioned) for row in q3_query_result]
    return output, q2_time_result