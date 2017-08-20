# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

init python:
    define.move_transitions("ease", 1.0)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show mint worried
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."
    show julius panning
    e "You've created a new Ren'Py game."

    hide julius
    show run_animation at truecenter with flash
    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    show mint happy at center behind run_animation with easeinright
    
    "Placeholder"
    show mint sad with dissolve
    
    "The end."
    # This ends the game.

    return
