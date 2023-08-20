

def precision(distance_list, label):
    success = 0
    count = 0
    for song in distance_list:
        if "label" in song:
            count += 1
        if song["label"] == label:
            success += 1
    return (success / count) * 100
        
