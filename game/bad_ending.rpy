label bad_ending:
    menu:
        "what kind of bad ending would you like?"
        "amnesia meltdown":
            jump bad_ending_amnesia
        "luka affection":
            jump bad_ending_affection

label bad_ending_amnesia:
    scene bg_hospital
    show marinette
    m "I'm having a meltdown"
    sp "Whenever amnesia reaches less than the meltdown threshold, the bad ending with Marinette having a meltdown triggers. CG: Marinette at the hospital?"
    jump endcard

label bad_ending_affection:
    scene bg_liberty
    show marinette at left
    show luka at right
    m "I'm running away with Luka"
    "If the Luka Affection meter is greater than the Luka threshold, then she runs away with Luka. CG: Polaroid picture of Marinette and Luka together."
    jump endcard
