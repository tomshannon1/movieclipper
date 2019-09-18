from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

times = [(80.300, 90.934), (91.000, 95.934), 
         (374.000, 382.934), (617.000, 619.934), (96.000, 106.934),
         (383.000, 396.934), (620.000, 629.934), (107.000, 118.934),
         (397.000, 416.934), (630.000, 637.937), (119.000, 122.934),
         (417.000, 434.000), (638.000, 642.000), (123.000, 140.000),
         (175.000, 206.934), (207.134, 213.934),
         (290.000, 295.000), (541.000, 545.934), (214.000, 219.934),
         (296.000, 300.934), (546.000, 548.934), (220.000, 223.934),
         (301.000, 303.934), (549.000, 549.934), (224.000, 225.934),
         (304.000, 318.000), (550.000, 556.000), (226.000, (241.000))

]
targets = ["level-0.mp4", "level-1.mp4", 
           "level-2-anger.mp4", "level-2-fear.mp4", "level-2-calm.mp4",
           "level-3-anger.mp4", "level-3-fear.mp4", "level-3-calm.mp4",
           "level-4-anger.mp4", "level-4-fear.mp4", "level-4-calm.mp4",
           "level-5-anger.mp4", "level-5-fear.mp4", "level-5-calm.mp4",
           "level-6.mp4", "level-7.mp4",
           "level-8-anger.mp4", "level-8-fear.mp4", "level-8-calm.mp4",
           "level-9-anger.mp4", "level-9-fear.mp4", "level-9-calm.mp4",
           "level-10-anger.mp4", "level-10-fear.mp4", "level-10-calm.mp4",
           "level-11-anger.mp4", "level-11-fear.mp4", "level-11-calm.mp4"
]


# For each desired subclip, list times and desired file names
for time, target in zip(times, targets):
    
    # Path to full film
    pathToFullFilm = "film.mp4"

    # Pull out sub clip from film 
    ffmpeg_extract_subclip(pathToFullFilm, time[0], time[1], targetname="filmclips/%s" % target)
    
    # Take subclip and pull out audio file
    video = VideoFileClip("filmclips/%s" % target)
    audio = video.audio
    audio.write_audiofile("audioclips/%s" % target.split('.')[0] + '.mp3')