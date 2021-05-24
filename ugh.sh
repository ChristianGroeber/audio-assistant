#!/bin/bash

set MUSIC_DIR = '/home/christian/Musik/'
set FLACS_DIR = 'flacs'
set OUT_DIR = 'out'

cd "$MUSIC_DIR"

if [ -d "out" ]; then
    rm -r "out"
fi

mkdir "out"

for dir in ./flacs/*/     # list directories in the form "/tmp/dirname/"
do
    dir=${dir%*/}      # remove the trailing "/"
    echo "/home/christian/Musik/flacs/${dir##*/}"    # print everything after the final "/"
    python3 /home/christian/PhpstormProjects/convert.py -d "/home/christian/Musik/flacs/${dir##*/}" --skip-spectrals
done
