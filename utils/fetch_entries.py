from utils.attributes import Attributes as attr
import utils.connect_db as db
import os

fetchable_attributes=[
    attr.CHROMA_SFT_MEAN,
    attr.CHROMA_SFT_VAR,
    attr.LABEL,
    attr.FILE_PATH,
    attr.RMS_MEAN,
    attr.RMS_VAR,
    attr.TEMPO,
    # attr.HARMONIC_MEAN,
    # attr.HARMONIC_VAR,
    # attr.SPECTRAL_CENTROID_MEAN,
    # attr.SPECTRAL_CENTROID_VAR,
    ]


def fetch_all_entries():
    columns = ""
    alias = "ta"
    query = ""
    for attribute in fetchable_attributes:
        column = f'{alias}.{attribute.value},  '
        columns += column

    columns = columns.rstrip(", ")
    query = f'SELECT {columns} FROM track_attributes {alias} ;'

    if query != "":
        return db.run_query(query)
    else:   
        return None
    
def serialize_response(response):
    serialized_response = []
    for row in response["rows"]:
        serialized_row = {}
        for index, column in enumerate(response["columns"]):
            if column == attr.FILE_PATH.value:
                # serialized_row[column] = row[index].replace("\\","/")
                serialized_row[column] = os.path.normpath(row[index])
            serialized_row[column] = row[index]
        serialized_response.append(serialized_row)
    return serialized_response
    