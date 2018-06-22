import os
import fnmatch

import config


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if not fnmatch.fnmatch(file, '*--conv.*'):
                if fnmatch.fnmatch(file.lower(), '*.aif') \
                or fnmatch.fnmatch(file.lower(), '*.wav') \
                or fnmatch.fnmatch(file.lower(), '*.mp3'):
                    r.append(os.path.join(root,file))

                elif fnmatch.fnmatch(file.lower(), '*.mid') \
                or fnmatch.fnmatch(file.lower(), '*.zip'):
                    pass
                else:
                    os.remove(os.path.join(root,file))

    return r

def remove_empty(mypath):
    for root, dirs, files in os.walk(mypath,topdown=False):
         for name in dirs:
             fname = os.path.join(root,name)
             if not os.listdir(fname):
                 print(fname)
                 os.removedirs(fname)

