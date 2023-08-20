from parse_dataset import parse_dataset
from connect_db import insert_song
import sys

folder_path_prefix = './dataset'

labels = ["blues","classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"]

def init_db():
    for label in labels:
        folder_path = folder_path_prefix + "/" + label
        new_songs = parse_dataset(folder_path)
        total_songs = len(new_songs)
        count = 0
        print(f"", end='\r')
        for song in new_songs:
            count += 1
            print(f"Writing item {count} of {total_songs} with label {label}", end='\r')
            sys.stdout.flush() 
            insert_song(song)

if __name__ == "__main__":
    init_db()