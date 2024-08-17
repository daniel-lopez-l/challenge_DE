from typing import List, Tuple
from time_utils import execute_time_query
from google.cloud import bigquery


def q2_time(client: bigquery.Client, query: str) -> Tuple[List[Tuple[str, int]], float]:
   
    """
    Execute and return the result of query and the time in ms
    Args:
        client (bigquery.Client),
        query (str)
    Returns: 
        result of query and the time in ms
    """
    
    q2_query_result, q2_time_result  = execute_time_query(client ,query)
    output = [(row.emoji, row.total_emoji) for row in q2_query_result]
    return output, q2_time_result