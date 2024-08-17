from typing import List, Tuple

<<<<<<< HEAD
@profile
def q2_memory(client: bigquery.Client, query: str) ->  List[Tuple[str, int]]:
    """
    Execute and return the result of query and the memory
    Args:
        client (bigquery.Client),
        query (str)
    Returns: 
        result of query
    """
    results = execute_query_for_memory(client, query)

    output = [(row.emoji, row.total_emoji) for row in results]

    return output
=======
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    pass
>>>>>>> main
