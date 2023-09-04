from moviepy.editor import VideoFileClip
import os 

files = os.listdir("dataset") 

# print(files) 
# Load the MPG video

path = "processed_dataset/" 

for file in files:
    mpg_video = VideoFileClip("dataset/"+file)  

    # Define the output file name and codec
    output_file = path+ file[:-4] + ".mp4" 
    codec = 'libx264'

    # Write the MPG video as an MP4 video
    mpg_video.write_videofile(output_file, codec=codec)

    # Close the video clip
    mpg_video.close() 