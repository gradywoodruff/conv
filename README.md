# Audio Conv
A mass converter for audio samples

### Starting Django
First create a new virtual env, and change directories

	virtualenv -p python3 audio_conv
	cd audio_conv

Add the new folder as the source make sure Pip is running in that folder

	source bin/activate
	which pip

Install django

	pip install numpy
	pip install pydub

Run a conv
	
	cd/app
	bin/run '/path/to/folder'