import os
import argparse
from helpers import get_audio_files, str2bool, get_metadata
import mutagen
import math


parser = argparse.ArgumentParser()
parser.add_argument('-d', help="The absolute Path to your Album")
parser.add_argument('--use-id3', help="Use Id3 Tags instead of File Name", type=str2bool, nargs='?', const=True, default=False)
parser.add_argument('--include-artist', help="Show the Artist name before the Track Name (needed for Albumns with different Artists) - This only applies when using --use-id3", type=str2bool, nargs='?', const=True, default=False)
args = parser.parse_args()

album = args.d
use_id3 = args.use_id3

for file in os.listdir(album):
    if os.path.isdir(os.path.join(album, file)) and file != '.' and file != '..':
        album = os.path.join(album, file)
print(album)

songs = get_audio_files(album)

album_information = "[size=4]Tracklist[/size]\n"

tracklist = [0]*len(songs)

for song in songs:
    name, ext = os.path.splitext(song)
    audio = mutagen.File(os.path.join(album, song))
    minutes = audio.info.length / 60 
    seconds = (minutes - math.floor(minutes)) * 60

    track_str = ""
    if use_id3:
        data = get_metadata(os.path.join(album, song))
        track_str = "[b]" + data['tracknumber'] + ".[/b]"
        if args.include_artist:
            track_str += " " + data['artist']
        track_str += " " + data['title']
    else:
        track_str = name 
    tracklist[int(audio['tracknumber'][0]) - 1] = track_str + " [i]" + str(math.floor(minutes)) + ':' + str(math.floor(seconds)) + "[/i]"

album_information += '\n'.join(tracklist)
print(album_information)


