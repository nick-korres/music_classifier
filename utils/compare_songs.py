from utils.fetch_entries import fetch_all_entries,serialize_response
from utils.parse_dataset import parse_single
from distance_calc.distance_funcs import distance_funcs



def compare_songs(input_song,func_name,threshold):
    response = fetch_all_entries()
    ser_res = serialize_response(response)

    parsed_input = parse_single(input_song)

    for song in ser_res:
        dist = distance_funcs[func_name](parsed_input,song)
        song["distance"] = dist

    sorted_res = sorted(ser_res, key=lambda k: k['distance'])
    return sorted_res[0:threshold]