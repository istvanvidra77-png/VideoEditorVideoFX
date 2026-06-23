from videofx import VideoClip, VideoEffects, Keyframe

clip = VideoClip("video.mp4")

# Create keyframe animation for brightness
brightness_effect = VideoEffects.brightness()
brightness_effect.set_keyframe(0, {"increase": 0})
brightness_effect.set_keyframe(5, {"increase": 30})
brightness_effect.set_keyframe(10, {"increase": 0})

clip.apply_effect(brightness_effect)
clip.export("animated_output.mp4")
