from typing import List, Tuple
from time_utils import execute_time_query
from google.cloud import bigquery


def q1_time(client: bigquery.Client, query: str) -> Tuple[List[Tuple[str, str]], float]:
    """
    Execute exetute_time_query functions for return the result of query and time
    Args:
        client (bigquery.Client),
        query (str)
    Returns: 
        result of query and the time in ms
    """
    q1_query_result, q1_time_result  = execute_time_query(client ,query)
    output = [(row.top_user, row.date) for row in q1_query_result]
    return output, q1_time_result