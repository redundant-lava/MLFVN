# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marinette")
define l = Character("Luka")
define a = Character("Adrien")

image marinette = im.Scale("marinette.png", 400, 700)
image adrien = im.Scale("adrien.png", 200, 600)
image catnoir = im.Scale("catnoir.png", 700, 700)
image ladybug = im.Scale("ladybug.png", 500, 700)
image luka = im.Scale("luka.png", 300, 700)

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

label bad_ending:
      menu:
          "what kind of bad ending would you like?"
          "amnesia meltdown":
              jump bad_ending_amnesia
          "luka affection":
              jump bad_ending_affection
      return

label bad_ending_amnesia:
      scene hospital
      show marinette
      m "I'm having a meltdown"
      "Whenever amnesia reaches less than the meltdown threshold, the bad ending with Marinette having a meltdown triggers. CG: Marinette at the hospital?"
      return
      
label bad_ending_affection:
      scene polaroid picture
      show marinette at left
      show luka at right
      m "I'm running away with Luka"
      "If the Luka Affection meter is greater than the Luka threshold, then she runs away with Luka. CG: Polaroid picture of Marinette and Luka together."
      return
      
label neutral_ending:

      scene airport

      show marinette

      m "he's just a good friend"

      "If the affection meter is less than 75 and the amnesia meter is above 75, she doesn’t remember and she doesn’t like him. NYC ending. He’s \“just a good friend!\” CG: Tearful goodbye at the airport."
      return

label happy_ending:
      scene paris
      show catnoir
      a "I'm Cat Noir"
      hide catnoir
      show adrien
      pause
      show marinette at left
      m "I love you"
      show kwamis at right
      hide marinette
      show ladybug at left
      m "I want to patrol"
      
      "If the affection meter is above a and the amnesia meter is between n and m, Adrien can transform in front of her and she remembers him and loves him. There’s a reunion with the Kwamis and Marinette transforms into Ladybug and tells Chat she wants to patrol. CG: LadyNoir swinging across the city. "
      return
      
label superhappy_ending:
      scene chapel
      show marinette
      m "I knew you were Chat"
      show adrien at right
      a "WHUT?! BUT HOW?"
      m ".. uh... you mean it wasn't obvious...?"
      a "Um, it was supposed to be a secret... right?"
      m "Literally no one else is as in love with me as you are. You are such a smitten kitten."
      "Solitude Date Trigger. If the affection meter is greater than 75 and the amnesia meter is below 50 but above 10, Marinette remembers and gets engaged to Adrien.” CG: Adrienette wedding."
      return

label true_ending:
      scene nyc
      show marinette
      m "Come to NYC with me!"
      "If the affection meter is above 75 and the amnesia meter is greater than or equal to 75, she doesn’t remember but loves him anyway. (“Come to NYC with me!”) CG: Them in NYC."
      return
