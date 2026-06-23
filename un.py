from videofx import VideoClip, VideoEffects

# Load a video file
video = VideoClip("path/to/video.mp4")

# Apply effects
video.apply_effect(VideoEffects.blur(radius=15))
video.apply_effect(VideoEffects.brightness(increase=20))
video.apply_effect(VideoEffects.saturate(factor=1.5))

# Export the edited video
video.export("output_video.mp4", fps=30, quality="high")
