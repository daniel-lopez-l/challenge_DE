from typing import List, Tuple, Any
import cProfile
import pstats
import time
from google.cloud import bigquery

def execute_time_query(client: bigquery.Client, query: str) -> Tuple[Any, float]:
    """
    Execute BigQuery and return the time of execution
    Args:
        client: bigquery.Client
        query (str)
    Returns: 
        result of query and the time in ms
    """
    profiler = cProfile.Profile()
    profiler.enable()
    
    start_time = time.time()
    
    query_job = client.query(query)
    query_job.result()
    results = query_job.result()
    
    end_time = time.time()
    execution_time = end_time - start_time
    profiler.disable()
    
    stats = pstats.Stats(profiler)
    stats.strip_dirs().sort_stats('cumtime').print_stats(10)
    
    return results, execution_time