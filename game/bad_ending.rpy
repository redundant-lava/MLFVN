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
      show marinette at left
      show luka at right
      m "I'm running away with Luka"
      "If the Luka Affection meter is greater than the Luka threshold, then she runs away with Luka. CG: Polaroid picture of Marinette and Luka together."
      return
      
