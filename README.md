# Audio Conv
A mass converter for audio samples

## Starting Conv
### First create a new virtual env, and change directories

	virtualenv -p python3 audio_conv
	cd audio_conv

### Add the new folder as the source make sure Pip is running in that folder

	source bin/activate
	which pip

### Install dependencies

    source bin/activate
    pip install -r requirements.txt

### Edit config
Change the name of `app/config_example.py` to `app/config.py` and edit any of the settings in it

### Run a conv
	
	bin/run /path/to/folder