# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marinette")
define l = Character("Luka")
define a = Character("Adrien")

image marinette = im.Scale("marinette.png", 320, 600)
image adrien = im.Scale("adrien.png", 200, 600)
image catnoir = im.Scale("catnoir.png", 700, 700)
image ladybug = im.Scale("ladybug.png", 500, 700)
image luka = im.Scale("luka.png", 260, 700)

image airport = im.Scale("airport.jpeg", 1280, 720)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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


