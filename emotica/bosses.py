import time
from texthelper import slowprint, slow_print, wait, prompt

def boss_puzzle(name, stat, player):
    slowprint(f"\nYou approach {name}. The world around you seems to hold its breath.")
    slowprint("The ground feels fragile beneath your feet, the shadows stretching longer and darker as you draw near.")
    slowprint("Every instinct screams that danger is near, yet something in you — a small, persistent part — wants to understand it, not run.")
    wait()

    if stat == "self_sabotage":
        slowprint("The Mirror of Doubt stands before you, jagged and blackened, yet reflecting your own face in strange, warped ways.")
        slowprint("Its eyes — your eyes — burn into your mind, making it impossible to look away.")
        slowprint('"You built your own walls, little dreamer," it hisses, voice scraping like stone against metal.')
        slowprint('"Each barrier, each fear, each doubt you tried to hide… they bind you more tightly than you realize."')
        slowprint('"Tell me… what is it that holds you back the most?"')
        ans = prompt(["Fear of failing", "Fear of trying", "Hope for better days"])
        if ans == 2:
            slowprint('"Yes… hope is not your chain," the mirror whispers. "You carry it freely, and it will guide you."')
            player.self_sabotage -= 2
            player.self_worth += 1
        else:
            # Expanded progressive dialogue for fear options
            fear_lines = [
                '"You still don’t see it," the mirror sighs, cracking slightly.',
                '"All this time, you have carried the weight of your failures as if they define you."',
                '"Every step you take, every choice you make, you shrink from your own potential, afraid to stumble, afraid to fall."',
                '"Do you not understand? Fear is not just a chain… it is a prison of your own making."',
                '"Look at yourself. Look at what you could be if you dared to let go of that fear."',
                '"Yet here you are, trembling before shadows, as if the world itself will punish you for trying."',
                '"You still don’t see the truth, little dreamer. And until you do… the walls remain, and so does the weight."'
            ]
            for line in fear_lines:
                slowprint(line)
            player.self_sabotage += 1

    elif stat == "stress":
        slowprint("Three enormous clocks hang in the sky, ticking at different, impossible speeds.")
        slowprint('"Which one do you follow?" whispers a voice, heavy with expectation.')
        ans = prompt(["The fastest", "The slowest", "Your heartbeat"])
        if ans == 2:
            slowprint('"Wise. Time isn’t the enemy when it beats inside you," the voice says, softening.')
            player.stress -= 2
            player.self_worth += 1
        else:
            slowprint("The clocks screech louder. Your chest tightens, each tick a reminder of pressure and expectation.")
            player.stress += 1

    elif stat == "anxiety":
        slowprint("A dense fog creeps forward, chilling your bones and whispering possibilities of disaster.")
        slowprint('"What if the worst happens?" it asks.')
        ans = prompt(["I’ll survive it", "It already is", "I don’t know"])
        if ans == 0:
            slowprint("The fog parts slightly, revealing shafts of light. Courage swells in your chest.")
            player.anxiety -= 2
            player.self_worth += 1
        else:
            slowprint("The fog deepens. Your heartbeat races; uncertainty coils tighter around you.")
            player.anxiety += 1

    elif stat == "self_worth":
        slowprint("A towering figure on a gray throne regards you silently, its gaze heavy, yet strangely patient.")
        slowprint('"What makes you real?" it asks, voice echoing through the hall like distant thunder.')
        ans = prompt(["My choices", "My pain", "Nothing"])
        if ans == 0:
            slowprint('"Then choose, and exist fully," it says. Light spreads through the hall.')
            player.self_worth += 2
        elif ans == 1:
            slowprint('"Pain can shape, but don’t let it rule," it whispers.')
            player.self_worth += 1
        else:
            slowprint("The hall grows darker. You feel small, almost lost in the shadows.")
            player.self_worth -= 2

    player.journal.append(f"Solved puzzle with {name}")

def mirror_of_doubt_intro(player):
    slowprint("\nA new presence emerges ahead — Mirror of Doubt. The air grows heavy, as if the world itself is holding its breath.")
    slowprint("The mirror stands tall and jagged, reflecting your face in strange, distorted ways.")
    slowprint("You feel the pull of your own fears staring back at you.")
    wait()
    boss_puzzle("Mirror of Doubt", "self_sabotage", player)

def clock_of_pressure_intro(player):
    slowprint("\nA new presence emerges ahead — Clock of Pressure. The air feels taut, almost vibrating with expectation.")
    slowprint("Three enormous clocks hang in the sky, ticking at impossible speeds.")
    slowprint("Your chest tightens as you hear a whisper: 'Which one do you follow?'")
    wait()
    boss_puzzle("Clock of Pressure", "stress", player)

def whispering_fog_intro(player):
    slowprint("\nA new presence emerges ahead — Whispering Fog. A dense, chilling mist swirls, wrapping around your legs like fingers.")
    slowprint("It whispers possibilities of disaster, and you feel your heartbeat quicken.")
    wait()
    boss_puzzle("Whispering Fog", "anxiety", player)

def gray_king_intro(player):
    slowprint("\nA massive, gray figure sits on a throne ahead — the Gray King. Its gaze pierces your very being.")
    wait()
    boss_puzzle("Gray King", "self_worth", player)
