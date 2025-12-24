"""
Supernatural / visual helpers: flashes, SFX helpers, PA glitches, transitions.
"""

init python:
    def play_sfx(sfx_file):
        """Play a sound effect from the sfx directory."""
        renpy.sound.play("sfx/" + sfx_file)
    def flash_screen(color="#FFFFFF", duration=0.2):
        """Flash the screen with a specified color and duration."""
        renpy.with_statement(renpy.transition(renpy.display.motion.Flash(color=color, duration=duration)))
    def glitch_effect(duration=0.5):
        """Apply a glitch effect for a specified duration."""
        renpy.with_statement(renpy.transition(renpy.display.motion.Glitch(duration=duration)))
    def fade_transition(duration=1.0):
        """Apply a fade transition for a specified duration."""
        renpy.with_statement(renpy.transition(renpy.display.motion.Fade(duration=duration)))

# Example usage in script:
# $ play_sfx("door_creak.ogg")
# $ flash_screen(color="#FF0000", duration=0.3)
# $ glitch_effect(duration=0.7)
# $ fade_transition(duration=1.5)
