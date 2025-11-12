import time
from texthelper import slowprint, slow_print, wait, prompt
def ending_scene(result, player):
    slowprint("\n--- EPILOGUE ---\n")
    
    if result == "good":
        # Hopeful / fully healed ending
        slowprint(f"{player.name} steps through the door again — this time fully awake. The air is sharp, crisp, and real, unlike any dream you’ve walked before.")
        slowprint("The sun warms your skin; the wind carries the scent of grass and distant flowers. Colors feel alive, vibrant, unfiltered.")
        slowprint("You pause for a moment, closing your eyes, feeling the simple joy of being present. Every choice you made, every fear you faced, led you here.")
        slowprint("The forest hums softly around you, but no shadow threatens you now. Even the faintest rustle of leaves feels like a gentle reminder that you survived, that you are growing.")
        slowprint("A distant figure smiles at you — perhaps one of the monsters, perhaps yourself in a reflection of your courage. You understand now: healing isn’t a destination; it’s the path you keep walking.")
        slowprint("With a deep breath, you step forward, lighter, yet grounded, ready to meet what comes next.")
        slowprint("\n✨ ENDING: HOPEFUL (GOOD) ✨")

    elif result == "neutral":
        # Balanced / acceptance ending
        slowprint("The meadow stretches endlessly, a mixture of dream and reality. You walk slowly, feeling the soft brush of grass against your hands.")
        slowprint("You glance back occasionally, remembering the paths you’ve taken — the struggles, the victories, the moments of doubt.")
        slowprint("You notice the little things now: the sway of flowers, the wind whispering through leaves, the warmth of sunlight on your face. They remind you that even amidst uncertainty, there is beauty.")
        slowprint("Your heart feels lighter than before, though the weight of your past still lingers. You’ve learned that balance is messy, but possible — a dance between fear and courage, hope and doubt.")
        slowprint("Sometimes, you pause to watch the sky change, letting yourself breathe. You smile softly, knowing you are learning to live with yourself, day by day.")
        slowprint("\n⚖️ ENDING: ACCEPTANCE (NEUTRAL) ⚖️")

    else:
        # Still struggling / bittersweet ending
        slowprint("You collapse beneath the weight of your thoughts. The meadow is soft around you, almost unreal, as if the world is cradling you in kindness despite your turmoil.")
        slowprint("The shadows of your fears still linger, stretching and twisting in ways you cannot fully escape. Your chest aches, heavy with everything you’ve carried.")
        slowprint("Yet even here, in this quiet despair, a faint light flickers in the distance. A gentle, patient reminder that the journey is not over — that another step, another try, is possible.")
        slowprint("You slowly push yourself up, feeling the cool grass under your hands and the wind on your face. It’s difficult, but you try to move forward, even if just a little.")
        slowprint("Perhaps you stumble again tomorrow, perhaps you will find courage when least expected. For now, you exist — fragile, uncertain, but alive. And that, for this moment, is enough.")
        slowprint("\n💤 ENDING: STILL STRUGGLING (BAD) 💤")

    # Show journal as a reflection of journey
    slowprint("\nYour JOURNAL reflects your journey:")
    for j in player.journal:
        print(" -", j)
    
    slowprint("\nThank you for playing *EMOTICA*. Remember: every ending is part of your story. Healing takes time, and every step forward matters.")
    slowprint("Reach out if this story resonated. You deserve light, even in the darkest moments.")
def determine_ending(player, battle_result):

    #Determines which ending the player gets based on stats and choices. Returns: "good", "neutral", or "bad"
    # If player stayed with Mother or high self_worth -> good
    if battle_result == "stay" or player.self_worth >= 7:
        return "good"
    # If player left but survived, medium stats -> neutral
    elif battle_result == "leave":
        return "neutral"
    # If player was defeated or low stats -> bad
    else:
        return "bad"


