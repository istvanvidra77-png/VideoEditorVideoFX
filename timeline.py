from videofx import Timeline, VideoClip

# Create a timeline
timeline = Timeline(fps=30, width=1920, height=1080)

# Add multiple clips
clip1 = VideoClip("video1.mp4")
clip2 = VideoClip("video2.mp4")

timeline.add_clip(clip1, start_time=0)
timeline.add_clip(clip2, start_time=5)

# Add transitions between clips
timeline.add_transition(0, 1, "dissolve", duration=1.0)

# Export final video
timeline.export("final_video.mp4")
