from videofx import VideoClip, VideoEffects

# Load and enhance a video
video = VideoClip("raw_footage.mp4")

# Enhance colors
video.apply_effect(VideoEffects.brightness(increase=10))
video.apply_effect(VideoEffects.saturate(factor=1.3))
video.apply_effect(VideoEffects.contrast(factor=1.2))

# Export
video.export("enhanced_footage.mp4", quality="high")
