# movieclipper

## Instructions
### Create virtual environment

```
conda create -n movieclip python=3.6
conda activate movieclip
pip install requirements.txt
```

### Create necessary folders
Add folders named filmframes, audioclips, filmclips

### Place your film asset in the folder and change paths
Place you film asset in the root directory (you can use what ever resolution file you want, but this will ultimately lead to large numpy arrays ~2-8 GB each if you run it in 4K. I have run it at 540 p to make the animation processing faster, but you might be able to get away with 1080 p — test and try), change the paths in movieclipper

### Specify times in movieclipper
Change the start and stop time tuples for each film asset. Do not change the names of the file names, as it will mess up the animation playback code. When you have the times specified run movieplayer. This will create a bunch of MP4 videos and MP3 audio files in videoclips and audioclips directories.

### Run clip parser
Change the file paths in this script to work with your computer. Run it and it will create 
numpy arrays of each film in filmframes directory. 