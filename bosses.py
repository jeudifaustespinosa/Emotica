import random
import time
from texthelper import slowprint, slow_print, wait, prompt

def boss_puzzle(name, stat, player):
    # Narrative intro before the choice
    slowprint(f"\nYou approach {name}. The world around you feels tense, as if it is holding its breath.")
    slowprint("Shadows stretch long, the ground beneath your feet seems to hum with anticipation.")
    slowprint("Every instinct screams danger, yet a small, stubborn curiosity keeps you moving forward.")
    wait()

    if stat == "self_sabotage":
        slowprint("The Mirror of Doubt towers ahead, jagged and blackened, reflecting your face in warped, uncanny ways.")
        slowprint("Its eyes — your eyes — pierce into your mind, impossible to look away from.")
        slowprint('"You built your own walls, little dreamer," it hisses, voice scraping like stone against metal.')
        slowprint('"Each barrier, each fear, each hidden doubt… binds you more tightly than you realize."')
        slowprint('"Tell me… what is it that holds you back the most?"')
        ans = prompt(["Fear of failing", "Fear of trying", "Hope for better days"])
        if ans == 2:
            slowprint('"Yes… hope is not your chain," the mirror whispers. "You carry it freely, and it will guide you."')
            player.self_sabotage -= 2
            player.self_worth += 1
        else:
            fear_lines = [
                '"You still don’t see it," the mirror sighs, cracking slightly.',
                '"All this time, you have carried the weight of your failures as if they define you."',
                '"Every step you take, every choice you make, you shrink from your own potential."',
                '"Do you not understand? Fear is not just a chain… it is a prison of your own making."',
                '"Look at yourself. Look at what you could be if you dared to let go of that fear."',
                '"Yet here you are, trembling before shadows, as if the world itself will punish you for trying."',
                '"You still don’t see the truth, little dreamer. And until you do… the walls remain, and so does the weight."'
            ]
            for line in fear_lines:
                slowprint(line)
            player.self_sabotage += 1

    elif stat == "stress":
        slowprint("Three enormous clocks hang in the sky, ticking at impossible, dissonant speeds.")
        slowprint('"Which one do you follow?" a voice whispers, heavy with expectation.')
        ans = prompt(["The fastest", "The slowest", "Your heartbeat"])
        if ans == 2:
            slowprint('"Wise choice. Time isn’t the enemy when it beats inside you," the voice says softly.')
            player.stress -= 2
            player.self_worth += 1
        else:
            slowprint("The clocks screech louder. Your chest tightens; each tick presses like a reminder of endless expectation.")
            player.stress += 1

    elif stat == "anxiety":
        slowprint("A dense, chilling fog coils around your legs, whispering possibilities of disaster.")
        slowprint('"What if the worst happens?" it murmurs.')
        ans = prompt(["I’ll survive it", "It already is", "I don’t know"])
        if ans == 0:
            slowprint("The fog parts slightly, revealing shafts of light. Courage swells inside you, a quiet warmth amidst the cold.")
            player.anxiety -= 2
            player.self_worth += 1
        else:
            slowprint("The fog deepens. Your heartbeat races, uncertainty tightening its grip on you.")
            player.anxiety += 1

    elif stat == "self_worth":
        slowprint("A gray throne looms, the figure atop staring with unwavering, silent patience.")
        slowprint('"What makes you real?" it asks, voice echoing through the hall like distant thunder.')
        ans = prompt(["My choices", "My pain", "Nothing"])
        if ans == 0:
            slowprint('"Then choose, and exist fully," it says. Light spreads through the hall, washing away shadows.')
            player.self_worth += 2
        elif ans == 1:
            slowprint('"Pain can shape, but do not let it rule," it whispers softly.')
            player.self_worth += 1
        else:
            slowprint("The hall grows darker. You feel small, almost lost in the vastness of the shadows.")
            player.self_worth -= 2

    # Append journal entry after each boss
    player.journal.append(f"Solved puzzle with {name}")

    # After-battle narrative
    slowprint(f"\nHaving faced {name}, you take a moment to breathe.")
    slowprint("Your thoughts swirl; the path ahead feels both heavy and promising.")
    slowprint("You continue walking, carrying the lessons of this encounter in the quiet of your heart.")
    wait()

def mirror_of_doubt_intro(player):
    slowprint("\nA presence emerges ahead — the Mirror of Doubt. The air feels heavy, almost suffocating.")
    slowprint("Its surface distorts your reflection, showing not only your face but your hidden fears.")
    wait()
    boss_puzzle("Mirror of Doubt", "self_sabotage", player)

def clock_of_pressure_intro(player):
    slowprint("\nAhead, the Clock of Pressure dominates the sky, immense and foreboding.")
    slowprint("Its hands move at impossible speeds; each tick echoes like a hammer on your chest.")
    wait()
    boss_puzzle("Clock of Pressure", "stress", player)

def whispering_fog_intro(player):
    slowprint("\nA thick, whispering fog rolls in, chilling your bones and wrapping the path in uncertainty.")
    slowprint("Every step feels heavier as invisible whispers tug at your mind.")
    wait()
    boss_puzzle("Whispering Fog", "anxiety", player)

def gray_king_intro(player):
    slowprint("\nThe Gray King sits atop his throne, immense and gray, his gaze cutting into your soul.")
    slowprint("A heavy silence fills the hall, broken only by your cautious footsteps.")
    wait()
    boss_puzzle("Gray King", "self_worth", player)

