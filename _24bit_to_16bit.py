import os
import argparse
import shutil


# parser = argparse.ArgumentParser()
# parser.add_argument('-d', help='Which Directory')
# args = parser.parse_args()

# folder = args.d
# os.chdir(folder)

# os.chdir('..')
# parent_dir = os.getcwd()

def down_encode(folder):
    old = folder + ' (24bit)'

    shutil.copytree(folder, old)
    os.chdir(folder)
    os.system('rm *.flac')

    os.chdir(old)
    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if ext != '.flac':
            continue   
        print("Now converting " + file)
        os.system("sox \"" + file + "\" -b16 \"" + folder + "/" + file + "\" rate -v -L 44100 dither")

# down_encode(folder)