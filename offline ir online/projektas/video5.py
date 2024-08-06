from moviepy.editor import VideoFileClip
import pygame
import sys
from subprocess import call

def play_video(video_source):
    # Load the video file
    clip = VideoFileClip(video_source)
    
    # Preview the video
    clip.preview()
    clip.close()
    pygame.quit()
    call(["python", "5lvl.py"])
    sys.exit()

if __name__ == "__main__":
    video_source = r'video\sviestas.mp4'  # Replace with your actual video file path
    play_video(video_source)