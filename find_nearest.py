from distance_calc.distance_funcs import DistanceFuncs
from distance_calc.precision import precision
from utils.compare_songs import compare_songs
import os

input_song = None
desired_label = None
k=None

def find_nearest():
    global input_song, desired_label, k
    if input_song is None:
        print("insert path to input song")
        input_song = input()

    if k is None:
        print("insert integer for k nearest")
        k = int(input())

    file_name = os.path.basename(input_song)
    out_dir=f"./out/{file_name}"
    ensure_directory(out_dir)

    for disc_func in DistanceFuncs:
        result = compare_songs(input_song,disc_func,k)
        output_file = f'{out_dir}/{disc_func.value}.json'
        with open(output_file,"w") as file:
            file.write(str(result))
        
        if desired_label is not None:
            prec = precision(result,desired_label)
            print(disc_func.value," precision: ",prec)


def ensure_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)            

if __name__ == "__main__":
    find_nearest()
