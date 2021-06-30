import audio_metadata
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', help='Directory to scan')
parser.add_argument('-f', help='File to scan')
args = parser.parse_args()

folder = args.d
file = args.f

print(folder)
print(file)

if folder is None and file is None:
    raise Exception('Either -d or -f have to be defined')

if folder is not None and not os.path.isdir(folder):
    raise Exception(folder + " is not a valid directory")

if file is not None and not os.path.isfile(file):
    raise Exception(file + " is not a valid file")


def get_metadata(f):
    data = audio_metadata.load(f)['tags']
    ret = {}
    for item in data:
        ret[item] = ', '.join(data[item])
    return data


if file is not None:
    print(get_metadata(file))
else:
    for f in os.listdir(folder):
        name, ext = os.path.splitext(f)
        if ext not in ['.flac', '.mp3']:
            continue
        print(get_metadata(os.path.join(folder, f)))
