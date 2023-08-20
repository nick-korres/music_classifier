import librosa
import os
import numpy as np
import json



attributes={ "duration": librosa.get_duration,
             "chroma_stft":librosa.feature.chroma_stft,
            "chroma_stft_mean":None,
            "chroma_stft_var":None,
            "rms":librosa.feature.rms,
            "rms_mean":None,
            "rms_var":None,
            "spectral_centroid":librosa.feature.spectral_centroid,
            "spectral_centroid_mean":None,
            "spectral_centroid_var":None,
            "spectral_rolloff":librosa.feature.spectral_rolloff,
            "spectral_rolloff_mean":None,
            "zero_crossing_rate":librosa.feature.zero_crossing_rate,
            "zero_crossing_rate_mean":None,
            "harmonic":librosa.effects.harmonic,
            "harmonic_mean":None,
            "harmonic_var":None,
            "perceptual_weighting":librosa.perceptual_weighting,
            "perceptual_weighting_mean":None,
            "perceptual_weighting_var":None,
            "tempo":librosa.beat.beat_track,
            "mfcc":librosa.feature.mfcc, 
            "mfcc_mean_1":None,
            "mfcc_var_1":None,
            "mfcc_mean_2":None,
            "mfcc_var_2":None,
            "mfcc_mean_3":None,
            "mfcc_var_3":None,
            "mfcc_mean_4":None,
            "mfcc_var_4":None,
            "mfcc_mean_5":None,
            "mfcc_var_5":None,
            "mfcc_mean_6":None,
            "mfcc_var_6":None,
            "mfcc_mean_7":None,
            "mfcc_var_7":None,
            "mfcc_mean_8":None,
            "mfcc_var_8":None,
            "mfcc_mean_9":None,
            "mfcc_var_9":None,
            "mfcc_mean_10":None,
            "mfcc_var_10":None,
            "mfcc_mean_11":None,
            "mfcc_var_11":None,
            "mfcc_mean_12":None,
            "mfcc_var_12":None,
            "mfcc_mean_13":None,
            "mfcc_var_13":None,
            "mfcc_mean_14":None,
            "mfcc_var_14":None,
            "mfcc_mean_15":None,
            "mfcc_var_15":None,
            "mfcc_mean_16":None,
            "mfcc_var_16":None,
            "mfcc_mean_17":None,
            "mfcc_var_17":None,
            "mfcc_mean_18":None,
            "mfcc_var_18":None,
            "mfcc_mean_19":None,
            "mfcc_var_19":None,
            "mfcc_mean_20":None,
            "mfcc_var_20":None,
            }



def parse_dataset(folder_path,out_dir=None):
    
    file_count = 0
    response=[]
    label= os.path.basename(os.path.normpath(folder_path))

    for filename in os.listdir(folder_path):
        output = None
        if filename.endswith('.wav'):
            file_count += 1
            print(f"Processing item {file_count} with label {label}", end='\r')
            audio_file_path = os.path.join(folder_path, filename)
            output = parse_single(audio_file_path,label)

            if(output is None):
                pass

            if out_dir is not None:
                with open(f"out/{out_dir}/sample_{file_count}.json", "w") as outfile:
                    arr= np.array(output)
                    temp = arr.tolist()
                    outfile.write(str(temp))
            else:
                response.append(output)

    return response

def parse_single(audio_file_path,label=""):
    output = {}
    norm_path = os.path.normpath(audio_file_path)
    try:
        audio_data, sample_rate = librosa.load(norm_path)
    except:
        return None

    for key in attributes:
        if attributes[key] is not None:

            if key == "rms" or key == "zero_crossing_rate" or key =="harmonic":
                output[key] = attributes[key](y=audio_data)
            elif key=="tempo":
                temp,_=attributes[key](y=audio_data, sr=sample_rate)
                output[key] = temp
            elif key =="perceptual_weighting":
                output[key] = attributes[key](S=audio_data, frequencies=sample_rate)
            else:
                output[key] = attributes[key](y=audio_data, sr=sample_rate)

            if key=="mfcc":
                for i in range(1,21):
                    output["mfcc_mean_"+str(i)] = np.mean(output["mfcc"][i-1])
                    output["mfcc_var_"+str(i)] = np.var(output["mfcc"][i-1])                        

            if key != "mfcc" and key !="duration" and key !="tempo":
                output[key+"_mean"] = np.mean(output[key])
                output[key+"_var"] = np.var(output[key])

            if isinstance(output[key],np.ndarray):
                del output[key]

    output["file_path"] = f"'{os.path.abspath(norm_path)}'"

    if(label!=""):
        output["label"] = f"'{label}'"
    else:
        output["label"] = f"{label}"

    return output