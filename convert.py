import os
import sys
import argparse
import shutil
import random
# import subprocess
# import soundfile as sf
# import numpy as np
# import lameenc as lame
import audio_metadata


def str2bool(v):
    if isinstance(v, bool):
            return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


# STEP 0: Setup
parser = argparse.ArgumentParser()
parser.add_argument('-d', help='Directory to convert')
parser.add_argument('--skip-spectrals', help='Do not create Spectrals', type=str2bool, nargs='?', const=True, default=False)
args = parser.parse_args()

folder = args.d
skip_spectrals = args.skip_spectrals

forms = {'320': '-b 320', 'V0': '-V 0'}

original = folder.split('/')[-1]

os.chdir(folder)
os.chdir('..')
parent_dir = os.getcwd()
spectral_dir = os.path.join(parent_dir, 'spectrals')
log_file = os.path.join(parent_dir, original + '.log')
final_dirs = [folder]
print(log_file)

def get_audio_files(directory, extensions = ['.flac', '.mp3']):
    files = []
    for file in os.listdir(directory):
        name, ext = os.path.splitext(file)
        if ext in extensions:
            files.append(file)
    return files

originals = get_audio_files(folder, ['.flac'])
os.chdir(folder)

# STEP 0.1: Get Metadata
metadata = {}
for file in originals:
    data = audio_metadata.load(os.path.join(folder, file))['tags']
    ret = {}
    for item in data:
        ret[item] = ', '.join(data[item])
    metadata[file] = ret

# STEP 1: Create spectrograms
if not skip_spectrals:
    print('Creating Spectrograms')
    if not os.path.isdir(os.path.join(spectral_dir, original)):
        os.mkdir(os.path.join(spectral_dir, original))
    os.chdir(folder)
    for file in originals:
        print('\t' + file)
        os.system('sox "' + file + '" -n remix 1 spectrogram -t \'' + file + '\' -x 3000 -y 513 -z 120 -w Kaiser -o "' + os.path.join(spectral_dir, original, file + '.png"'))
        os.system('sox "' + file + '" -n remix 1 spectrogram -t \'' + file + '\' -X 500 -y 1025 -z 120 -w Kaiser -S 1:00 -d 0:02 -o "' + os.path.join(spectral_dir, original, file + '-zoom.png"'))
else:
    print('Not creating Spectrograms')

os.chdir('..')

# STEP 2: Convert flac's
for form in forms:
    current = os.getcwd()
    new = original + ' (' + form + ')'
    print(new)
    shutil.copytree(original, new)
    os.chdir(new)
    os.system('rm *.flac')
    for file in originals:
        name, ext = os.path.splitext(file)
        print(name)
        # subprocess.call(["lame", "-S ", forms[form], os.path.join(folder, file), name + ".mp3"])
        # subprocess.run("lame -S " + forms[form] + " '" + os.path.join(folder, file) + "' '" + os.path.join(os.getcwd(), name + ".mp3") + "'")
        data = metadata[file]
        os.system("lame -S " + forms[form] + " \"" + os.path.join(folder, file) + "\" \"" + name + ".mp3\" --tt \"" + data['title'] + "\" --ta \"" + data['artist'] + "\" --tl \"" + data['album'] + "\" --ty \"" + data['date'] + "\" --tn " + data['tracknumber'])
    os.chdir(current)
    final_dirs.append(os.path.join(parent_dir, new))

# STEP 3: Create the .torrent file
os.chdir(parent_dir)
for directory in final_dirs:
    if os.path.isfile(directory + '.torrent'):
        os.remove(directory + '.torrent')
    os.system('mktorrent "' + directory + '"')
