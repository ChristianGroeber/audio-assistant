# Help with Audio Files
Edit Metatags and automatically generate convert flac's to mp3

## Usage

### Convert 24bit Flac to 16bit Flac
Call the File `24bit_to_16bit.py` with the Argument `-d` as the absolute Path to the Album you'd like to convert.
This creates a Subfolder `16bit` inside the album with the converted files inside it

**Example:**
`python3 24bit_to_16bit.py -d '/home/christian/Musik/Justin Bieber - Baby'`

#### Parameters
Parameter | Description
--- | ---
`-d` | The Absolute Path to your Album 

### Encode Flac to MP3
Encode an Album from Flac to MP3 in both 320 CBR and V0 VBR, plus create a spectral analysis of the original files

**Example:**
`python3 convert.py -d '/home/christian/Musik/Justin Bieber - Baby'`

This creates 2 new Folders in `/home/christian/Musik`, called `Just Bieber - Baby (320)` and `Justin Bieber - Baby (V0)`

Upon the first time running this command, it will also create a directory named `spectrals` in `/home/christian/Musik`, and adds a new folder with the same name as the original album, with the spectral files within.

#### Parameters
Parameter | Description
--- | ---
`-d` | The Absolute Path to your Album
`--skip-spectrals` | Do not create Spectral Analysis

### Edit id3 Tags
Edit the tags of all songs inside an Album

`python3 id3_helper.py '/home/christian/Musik/Justin Bieber - Baby'`

This will prompt you to Enter Artist, Album Name, and Release Year. 

**Important**
This currently only works with Flac Files

#### Parameters
Name | Description
--- | ---
`-d` | The Absolute Path to your Album
`--overwrite-existing` | Also overwrite existing Tags

## Dependencies
- `audio-metadata`
- `mutagen`
- `lame`

### Installation
`pip install audio-metadata mutagen`
`sudo apt install -y lame`