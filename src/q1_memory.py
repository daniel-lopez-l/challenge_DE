from typing import List, Tuple
from datetime import datetime
from google.cloud import bigquery

def q1_memory(client: bigquery.Client(), query:str) -> List[Tuple[str, str]]:
    # Ejecutar la consulta
    query_job = client.query(query)


    query_job.result()
    results = query_job.result()
    output = [(row.top_user, row.date) for row in results]

   
    # print("QUERY 1")
    # print ("Las top 10 fechas donde hay más tweets. Ordenadas por usuario (username) que más publicaciones tiene por cada uno de esos días: ")
    # print(output)
    return output