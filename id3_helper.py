import argparse
import os
from helpers import get_audio_files, str2bool
from mutagen.flac import FLAC


parser = argparse.ArgumentParser()
parser.add_argument('-d', help="The absolute Directory of the Album")
parser.add_argument('--overwrite-existing', help='Overwrite Existing Tags', type=str2bool, nargs='?', const=True, default=False)
args = parser.parse_args()

album = args.d
overwrite = args.overwrite_existing

data = {}
tags = ['artist', 'date', 'album']

# General Information
print('Artist Name')
data['artist'] = input()

print('Album Name')
data['album'] = input()

print('Year')
data['date'] = input()

files = get_audio_files(album, ['.flac'])

for file in files:
    audiofile = FLAC(os.path.join(album, file))
    print(audiofile)
    for tag in tags:
        tag_exists = tag in audiofile
        if not tag_exists or overwrite:
            audiofile[tag] = data[tag]
    audiofile.save()

