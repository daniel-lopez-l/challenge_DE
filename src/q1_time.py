from typing import List, Tuple
import cProfile
import pstats
import time
from google.cloud import bigquery


def q1_time(client: bigquery.Client, query: str) -> Tuple[List[Tuple[str, str]], float]:
    profiler = cProfile.Profile()
    profiler.enable()
    
    start_time = time.time()
    
    query_job = client.query(query)
    query_job.result()
    results = query_job.result()
    
    output = [(row.top_user, row.date) for row in results]

    end_time = time.time()
    execution_time = end_time - start_time
    profiler.disable()
    
    stats = pstats.Stats(profiler)
    stats.strip_dirs().sort_stats('cumtime').print_stats(10)  # Mostrar las 10 líneas más lentas

    print(f"Tiempo total de ejecución: {execution_time:.2f} segundos")
    
    return output, execution_time