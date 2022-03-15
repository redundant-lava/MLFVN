# The script of Chapter 01
label ch_01:
    scene bg_hospital

    sp "Marinette is in the hospital and Adrien panics. Gives exposition to Alya about what happened to her (she willingly gave up the Miracle Box in the fight with Shadowmoth to save Chat), and says he got there \“as soon as I could\” after Alya called saying Marinette was awake."

    show adrien confused at left

    ## Decision CR2 ###########
    $ scores = ["aff += 1", "aff -= 1; amn -= 1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "who should go in the room first?"
        "Alya \u27A4 [hints[0]]":
            $ exec(scores[0])
            jump CR2_alya
        "Adrien \u27A4 [hints[1]]":
            $ exec(scores[1])
            jump CR2_adrien

label CR2_alya:
    scene bg_hospital_bathroom
    show adrien neutral
    show kwamis at right
    sp "Adrien talks to the Kwamis in the bathroom of the hospital and calms down."
    hide kwamis
    hide adrien
    jump CR3

label CR2_adrien:
    show adrien confused at center
    show marinette happy at left #TODO: show marinette scared at left
    sp "Adrien scares the crap out of Marinette because he's so worried."

label CR3:
    scene bg_hospital
    sp "Adrien figures out how much Marinette remembers, which is nothing at all. Flashback to the LadyNoir proposal scene (\“ask me again after we defeat Shadow Moth, Kitty.\”)"
    show adrien confused at right
    ## Decision CR4 ###########
    $ scores = ["amn += 50", "aff += 1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "Should I reveal my identity?"
        "Yes \u27A4 [hints[0]]":
            $ exec(scores[0])
            jump bad_ending_amnesia
        "No \u27A4 [hints[1]]":
            sp "Remembering Fu having a nervous breakdown, Adrien decides against revealing his identity"
            $ exec(scores[1])
            jump CR5

label CR5:
    scene bg_adrien_room
    show adrien confused at left
    $ scores = ["aff += 1", "aff -= 1; Laff += 1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "Should I get Advice from the Kwamis or advice from my mom?"
        "Kwamis \u27A4 [hints[0]]":
            scene bg_adrien_room
            sp" The Kwamis give Adrien advice."
            $ exec(scores[0])
            if aff >= 3:
                sp "affection meter >= 3. the Kwamis tell him he’s doing the right thing"
            else:
                sp "aff less than 3, the Kwamis tell him to shape up."
            jump CR6
        "Mom \u27A4 [hints[1]]":
            scene bg_graveyard
            sp "Adrien visits his mother’s gravestone and doesn’t know what to do."
            $ exec(scores[1])
            jump CR6

label CR6:
    scene bg_adrien_room
    show adrien neutral at left
    sp "Marinette calls Adrien and tells him she’s going to NYC. She’s been invited to the Fashion Institute. She’s also been invited to the Liberty with Luka and asks Adrien to come."
    $ scores = ["Laff += 1", "aff +=1", "aff -= 1; Laff += 1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "How should I respond?"
        "I have plans. \u27A4 [hints[0]]":
             $ exec(scores[0])
             jump CR7
        "Sounds awesome! \u27A4 [hints[1]]":
             $ exec(scores[1])
             jump CR8
        "Seriously? With the way Kitty Section plays? \u27A4 [hints[2]]":
             $ exec(scores[2])
             jump CR7

label CR7:
    scene bg_adrien_room
    show adrien neutral at left
    sp "Adrien mopes around at home. He calls Marinette, who is hanging out with Luka, so she doesn’t answer."
    $ scores = ["aff -= 1; amn -=1; Laff +=1", "aff-=1; Laff+=1", "aff += 1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "What should I do?"
        "Call her again and again until she answers \u27A4 [hints[0]]":
            sp "Marinette again invites Adrien to the Liberty, which he accepts."
            $ exec(scores[0])
            jump CR8
        "Leave her alone \u27A4 [hints[1]]":
            $ exec(scores[1])
            jump CR12
        "Talk to the Kwamis \u27A4 [hints[2]]":
            sp "Adrien decides to go to the Liberty to see her."
            $ exec(scores[2])
            jump CR8

label CR8:
    scene bg_liberty
    show marinette happy at left
    show luka at center
    show adrien happy at right
    sp "Adrien enjoys his time with Luka. So does Marinette. Luka asks Adrien a question:"
    l "What is your favorite ice cream?"
    $ scores = ["aff-=1; amn -=1", "aff +=1; amn-=1", "aff-=1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "What should I tell Luka about my favorite ice cream?"
        "Ladybug-themed \u27A4 [hints[0]]":
            sp "Adrien rattles off the Ladybug-themed ice cream and why (has a crush on Ladybug)."
            $ exec(scores[0])
            jump CR9
        "Passionfruit \u27A4 [hints[1]]":
            sp "Adrien’s favorite. He’s cute when he gushes."
            $ exec(scores[1])
            jump CR9
        "Peanut butter \u27A4 [hints[2]]":
            sp "Marinette hates that flavor and wouldn’t kiss anyone who tasted like peanut butter."
            $ exec(scores[2])
            jump CR9

label CR9:
    scene bg_liberty
    show luka at center
    show marinette happy at left
    show adrien neutral happy at right
    l"I just don't want anyone to take advantage of Marinette without you knowing who she can and can't trust,"
    sp " this is making Marinette wary of Adrien. The heroes get mentioned. Marinette asks about them."
    m "Did you know the heroes, Adrien?"
    $ scores = ["aff+=1; amn -=1", "amn-=1", "aff -= 1; Laff += 1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "What should I tell Marinette?"
        "We used to be very close. \u27A4 [hints[0]]":
            $ exec(scores[0])
            jump CR10
        "I didn’t know Ladybug as well as I would have liked. \u27A4 [hints[1]]":
            $ exec(scores[1])
            jump CR10
        "No, I didn’t know them at all. \u27A4 [hints[2]]":
            $ exec(scores[2])
            jump CR10

label CR10:
    scene bg_liberty
    show adrien neutral at right
    $ scores = ["aff += 1; amn -= 1", "aff += 0"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "Ask to take Marinette home?"
        "Yes. \u27A4 [hints[0]]":
            $ exec(scores[0])
            sp "Adrien asks."
            if aff > amn:
                if persistent.difficulty == 0:
                    $ renpy.say(dev, "affection  " + str(aff) + " is greater than amnesia " + str(amn))
                sp " Marinette says yes."
                jump CR11
            else:
                if persistent.difficulty == 0:
                    $ renpy.say(dev, "affection " +str(aff) + " is less than or equal to amnesia " + str(amn))
                sp "Marinette says no."
                jump CR12
        "No. \u27A4 [hints[1]]":
            $ exec(scores[1])
            sp "Adrien leaves."
            jump CR12

label CR11:
    scene bg_marinette_room

    sp "Marinette and Adrien have a good time in her room."
    #$ aff+=1; amn-=1
    show adrien neutral happy at right
    $ scores = ["aff+=1; amn -=1", "aff -=1; Laff += 1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "should I kiss her knuckles goodbye?"
        "Yes. \u27A4 [hints[0]]":
            $ exec(scores[0])
            sp "Adrien asks."
            if aff >= amn:
                if persistent.difficulty == 0:
                    $ renpy.say(dev, "affection " + str(aff) + " is graterthan or equal to Amnesia " + amn)
                sp "Marinette says yes."
                jump CR12
            else:
                if persistent.difficulty == 0:
                    $ renpy.say(dev, "affection " + str(aff) + " is less than Amnesia " + amn)
                sp "Marinette says no."
                jump CR12
        "No. \u27A4 [hints[1]]":
            $ exec(scores[1])
            sp "Adrien doesn’t ask."
            jump CR12

label CR12:  #TODO missing from Cass's outline?
    jump CR13

label CR13:
    scene bg_placedesvosges
    sp "Adrien after a photoshoot or something."
    show marinette happy at left
    m "Me and the girls were going to help out at an animal shelter."
    show adrien neutral happy at right
    $ scores = ["aff-=1", "aff+=1", "aff-=1"]
    $ hints = ["", ""]
    if persistent.difficulty == 0:
        $ hints = scores
    menu:
        "How should I respond?"
        "Hope you have fun with that. \u27A4 [hints[0]]":
            $ exec(scores[0])
            "..."
        "Do you need any help? \u27A4 [hints[1]]":
            $ exec(scores[1])
            "..."
        "I'm tired, I'm heading home \u27A4 [hints[2]]":
            $ exec(scores[2])
            "..."
    sp "Regardless of what you do, you end up going home, as picking B will lead to her sending you home and insisting you need rest anyway."
    jump CR14

label CR14:
    scene bg_adrien_room
    show adrien neutral at left
    sp "He calls Alya and asks her how Marinette is doing. Alya reminds Adrien of his time clock and tells him he has x amount of days left before Marinette leaves for NYC."
    if amn > -2:
        if persistent.difficulty == 0:
            $ renpy.say(dev, "Amnesia " + str(amn) + " is > -2")
        sp "Alya tells him that she’s not remembering anything and asks Adrien what he’s going to do."
        a "I'll ask her out on a date"
    else:
        if persistent.difficulty == 0:
            $ renpy.say(dev, "Amnesia " + str(amn) + " is <= -2")
        sp "Alya tells him that she’s doing great, but things could be better. She asks Adrien what he’s going to do."
        a "I'll ask her out on a date"
    jump ch_02
