import os
import sys
import pydub
import glob
import fnmatch
import datetime

import config
from actions import list_files, remove_empty

target_dir = sys.argv[1]
tags = {}

if config.ARTIST_NAME:
    tags['artist'] = config.ARTIST_NAME
if config.ALBUM_NAME:
    tags['album'] = config.ALBUM_NAME

for file in list_files(target_dir):
    try:
        conv_file = os.path.splitext(file)[0] + '--conv.aif'
        if fnmatch.fnmatch(file, '*.wav'):
            sound = pydub.AudioSegment.from_wav(file)
        elif fnmatch.fnmatch(file, '*.mp3'):
            sound = pydub.AudioSegment.from_mp3(file)
        elif fnmatch.fnmatch(file, '*.aif'):
            sound = pydub.AudioSegment.from_file(file)

        sound.export(conv_file, format=config.OUTPUT_FORMAT, bitrate=config.OUTPUT_BITRATE, tags=tags)
    except:
        pass

    os.remove(file)

remove_empty(target_dir)
