from videofx import VideoClip, VideoEffects, Timeline

# Create a video clip
clip = VideoClip("input.mp4")

# Build an effects chain
clip.apply_effect(VideoEffects.blur(radius=10))
clip.apply_effect(VideoEffects.brightness(increase=15))
clip.apply_effect(VideoEffects.contrast(factor=1.3))
clip.apply_effect(VideoEffects.saturate(factor=1.2))

# Add transitions
clip.add_transition("fade", duration=1.0)

# Add text overlay
clip.add_text("VideoFX Editor", position=(50, 50), fontsize=48)

# Export with specific settings
video.export("output.mp4", 
             fps=30, 
             bitrate="5000k",
             quality="high",
             audio=True)
