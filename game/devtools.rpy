"""
Dev-only overlay screen showing affinities + optional jump menu for quick testing.
"""

screen devtools_overlay():
    tag devtools
    zorder 1000

    frame:
        style "devtools_frame"
        xalign 0.98
        yalign 0.02
        xpadding 10
        ypadding 10

        vbox:
            text "Devtools Overlay" style "devtools_title"

            # Display affinities for characters
            text "Alex Affinity: [get_affinity('alex')]" style "devtools_affinity"
            text "Sam Affinity: [get_affinity('sam')]" style "devtools_affinity"
            text "Rin Affinity: [get_affinity('rin')]" style "devtools_affinity"

            # Quick jump buttons for testing scenes
            text "Quick Jumps:" style "devtools_title"
            button:
                style "devtools_button"
                text "Jump to Alex Scene"
                action Jump("alex_scene_label")
            button:
                style "devtools_button"
                text "Jump to Sam Scene"
                action Jump("sam_scene_label")
            button:
                style "devtools_button"
                text "Jump to Rin Scene"
                action Jump("rin_scene_label")

# Helper function to get affinity
init python:
    def get_affinity(character):
        """Get the affinity of a character."""
        global_vars = renpy.store
        if character == "alex":
            return global_vars.alex_affinity
        elif character == "sam":
            return global_vars.sam_affinity
        elif character == "rin":
            return global_vars.rin_affinity
        else:
            return 0

# Styles for the devtools overlay
style devtools_title:
    size 24
    bold True
    color "#FFFFFF"
    xalign 0.5
    ypadding 10

style devtools_affinity:
    size 18
    color "#FFFFFF"
    ypadding 5
style devtools_button:
    size 16
    background "#444444"
    color "#FFFFFF"
    padding (5, 10)
    hover_background "#666666"
    hover_color "#FFFFFF"
    ypadding 5

# Example of how to show the devtools overlay
# $ renpy.show_screen("devtools_overlay")
