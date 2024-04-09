# Minecraft Auto Fisher

Automatically fish in Minecraft

I forked this because the original stopped working. I really don't know python, and I don't know the proper way to use github. This is my best effort.

2024-04-09 - Updated to work on Python 3.12, and embed the image-to-match (imgur no longer returns a PNG when querying the url)

## How to use (simple) in Windows

1. Double click the downloaded file
2. Turn on subtitles in Minecraft and make sure language is English
3. Start fishing - it will continue automatically
4. Press `F12` to quit the program

## How to use with Python (advanced)

1. Make sure you have Python 3.12 or greater installed and accesible from the command-line
2. download fishing.py from this repo
3. 3. Run `python fishing.py` in the directory where the script was downloaded
4. (Bonus) Compile to an executable: create a virtualenv, install requirements.txt, `pyinstaller --onefile fishing.py`
