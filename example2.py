from videofx import VideoClip, VideoEffects
import os

# Process all videos in a folder
input_folder = "raw_videos"
output_folder = "processed_videos"

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"enhanced_{filename}")
        
        video = VideoClip(input_path)
        video.apply_effect(VideoEffects.brightness(increase=15))
        video.apply_effect(VideoEffects.saturate(factor=1.2))
        video.export(output_path)
        
        print(f"Processed: {filename}")
