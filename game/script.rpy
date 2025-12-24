# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define devtools_overlay = "devtools_overlay"



# The game starts here.

label start:
    scene bg room
    $ renpy.show_screen(devtools_overlay)


    mc "This is the main character speaking."
    alex "Hi, I'm Alex!"
    sam "Hello, I'm Sam."
    rin "Hey there, I'm Rin."

    $ renpy.hide_screen(devtools_overlay)
    stranger "Greetings, I am the Stranger."
    
    return
