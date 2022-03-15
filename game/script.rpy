# The script of the game goes in this file.
default persistent.difficulty = 1
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marinette", color='#fc94ad')
define l = Character("Luka", color ='#4c8087')
define a = Character("Adrien", color='#154b00')
define sp = Character("SCREEN PLAY") #temporary charater for script notes
define dev = Character("DEVELOPER NOTES", color='#ff180a')

# declare character meters
default amn = 0  # amnesia meter
default aff = 0  # affection meter (adrien)
default Laff= 0  # Luka affection meter

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg_marinette_room

    # This shows a character sprite.
    show marinette happy at left
    m "Welcome to the MLFVN!"
    sp "This is the SCREEN PLAY. It displays notes from the script outline for sections that do not have a finished script. It will not be visible during the final game."
    # These display lines of dialogue.
    menu:
        "This game is still in development. Chose a chapter to jump to."
        "Chapter 1 (OUTLINE ONLY)":
            jump ch_01
        "Endings (good // neutral // bad // true)":
            jump endings

label endcard:
    scene bg_paris
    if persistent.difficulty == 0:
        dev "This is a developer screen only for debug purposes. Final scores for this chapter:"
        $ renpy.say(dev, "Amnesia Meter: " + str(amn) + " // Affection Meter: " + str(aff) + " // Luka Affection meter: " + str(Laff))
    "THE END"
    return

label endings:
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
