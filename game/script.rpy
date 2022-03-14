# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marinette")
define l = Character("Luka")
define a = Character("Adrien")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite.


    show marinette at left

    # These display lines of dialogue.
    menu:
        "what kind of ending would you like?"
        "bad":
            jump bad_ending
        "neutral":
            jump neutral_ending
        "happy":
            jump happy_ending
        "super happy":
            jump superhappy_ending
        "true":
            jump true_ending


