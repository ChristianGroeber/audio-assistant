import os
import argparse
from helpers import get_audio_files, str2bool
import mutagen
import math


parser = argparse.ArgumentParser()
parser.add_argument('-d', help="The absolute Path to your Album")
parser.add_argument('--use-id3', help="Use Id3 Tags instead of File Name", type=str2bool, nargs='?', const=True, default=False)
args = parser.parse_args()

album = args.d

songs = get_audio_files(album)

album_information = "[size=4]Tracklist[/size]\n"

tracklist = [0]*len(songs)

for song in songs:
    name, ext = os.path.splitext(song)
    audio = mutagen.File(os.path.join(album, song))
    minutes = audio.info.length / 60 
    seconds = (minutes - math.floor(minutes)) * 60
    tracklist[int(audio['tracknumber'][0]) - 1] = name + " " + str(math.floor(minutes)) + ':' + str(math.floor(seconds))

album_information += '\n'.join(tracklist)
print(album_information)


