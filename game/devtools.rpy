# Dev-only overlay screen showing affinities + truth_score + quick jumps.

init python:
    # Only show this overlay in developer mode.
    if not hasattr(config, "overlay_screens"):
        config.overlay_screens = []
    if "devtools_overlay" not in config.overlay_screens:
        config.overlay_screens.append("devtools_overlay")

screen devtools_overlay():

    # Hide overlay in non-developer builds.
    if not config.developer:
        pass

    frame:
        style_prefix "devtools"
        xalign 0.98
        yalign 0.02

        vbox:
            text "DEV" size 16

            text "rin: [affinity['rin']]" 
            text "sam: [affinity['sam']]" 
            text "alex: [affinity['alex']]" 
            text "stranger: [affinity['stranger']]"
            text "truth: [truth_score]"

            textbutton "Jump: Prologue" action Jump("prologue")
            textbutton "Jump: Chapter 1 (Rin)" action Jump("chapter1")

# Styles for the overlay
style devtools_frame is frame:
    background "#000000CC"
    padding (10, 10)

style devtools_vbox is vbox:
    spacing 4

style devtools_text is text:
    size 14
    color "#FFFFFF"

style devtools_button is button:
    padding (4, 8)
    background "#444444"
    hover_background "#666666"

style devtools_button_text is text:
    size 12
    color "#FFFFFF"
