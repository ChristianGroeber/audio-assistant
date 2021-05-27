import os
import argparse
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('-d', help='Which Directory')
args = parser.parse_args()

folder = args.d
os.chdir(folder)

if os.path.isdir('16bit'):
    shutil.rmtree('16bit')
os.mkdir('16bit')

for file in os.listdir():
    name, ext = os.path.splitext(file)
    if ext != '.flac':
        continue   
    print("Now converting " + file)
    os.system("sox \"" + file + "\" -b16 \"16bit/" + file + "\" rate -v -L 48000 dither")