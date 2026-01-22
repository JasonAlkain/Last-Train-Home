# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define devtools_overlay = "devtools_overlay"



# The game starts here.

label start:
    # Show the devtools overlay for testing
    $ renpy.show_screen(devtools_overlay)

    # Shop blackout transition
    scene black
    with dissolve

    call rt_start from _call_rt_start

    return
