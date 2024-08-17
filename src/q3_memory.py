from typing import List, Tuple

<<<<<<< HEAD
@profile
def q3_memory(client: bigquery.Client, query: str) ->  List[Tuple[str, int]]:
    """
    Execute and return the result of query and the memory
    Args:
        client (bigquery.Client),
        query (str)
    Returns: 
        result of query
    """
    results = execute_query_for_memory(client, query)

    output = [(row.top_mentioned, row.total_mencioned) for row in results]

    return output
=======
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    pass
>>>>>>> main
