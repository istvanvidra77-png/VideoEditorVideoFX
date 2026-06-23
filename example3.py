from videofx import VideoClip, VideoEffects

video = VideoClip("intro.mp4")

# Fade in effect
video.apply_effect(VideoEffects.fade(duration=2.0))

# Add title
video.add_text("My Awesome Video", 
               position=("center", "center"),
               fontsize=72,
               color="white",
               duration=4.0)

# Zoom transition at the end
video.apply_effect(VideoEffects.zoom(duration=1.5, scale=1.2))

video.export("intro_with_effects.mp4")
