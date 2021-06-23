import os
import argparse
import audio_metadata

def get_audio_files(directory, extensions = ['.flac', '.mp3']):
    files = []
    for file in os.listdir(directory):
        name, ext = os.path.splitext(file)
        if ext in extensions:
            files.append(file)
    return files


def str2bool(v):
    if isinstance(v, bool):
            return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_metadata(track):
    data = audio_metadata.load(track)['tags']
    ret = {}
    for item in data:
        ret[item] = ', '.join(data[item])
    return ret