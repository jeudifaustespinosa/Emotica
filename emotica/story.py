import time
from texthelper import slowprint, slow_print, wait, prompt
from characters import talk_to_npc
from bosses import boss_puzzle, mirror_of_doubt_intro, clock_of_pressure_intro, whispering_fog_intro, gray_king_intro

def cinematic_intro(player):
    slow_print("《 EMOTICA 》", 0.07)
    time.sleep(1.5)
    slow_print("\nA story about healing, fear, and self-understanding.\n")
    wait()
    
    
    slow_print(f"\n{player.name}... huh. Nice name.")

    wait()
    
    slow_print("\nSometimes the people around you won’t understand your journey...")
    time.sleep(1.5)
    slow_print("They don’t need to — it’s not for them.")
    wait()
    
    slow_print("\nA sharp pain echoes in your head.")
    slow_print("You open your eyes... but nothing looks familiar.")
    wait()
    
    slow_print("A gray road stretches endlessly ahead.")
    slow_print("Green grass waves gently around you.")
    slow_print("And a bed of yellow flowers glows softly under a pale sky.")
    wait()
    
    slow_print(f"{player.name}: Where... am I?")
    time.sleep(1)
    slow_print("The air feels heavy. It’s quiet — too quiet.")
    wait()
    
    slow_print("You take a step forward, unsure whether this is a dream...")
    slow_print("...or something else entirely.")
    wait()
    print("\n[Scene: You begin walking down the road...]\n")
    wait()
    slow_print("Suddenly, a creature appears — a monster, but kind-looking.")
    slow_print("Her eyes are soft, her presence gentle.")
    wait()
    slow_print("The character sees the kind monster and she approaches, saying softly, 'This way.'")
    wait()

    slow_print("You follow the monster through the RUINS, passing under a huge door, big enough for the monster to enter as well.")
    wait()

    slow_print('"Welcome to your new home, innocent one," she says gently.')
    slow_print('"Allow me to educate you in the operation of the RUINS."')
    wait()

    slow_print("She explains as you follow, 'The RUINS are full of puzzles. Ancient fusions between diversions and doorkeys.'")
    slow_print('"One must solve them to move from room to room. Please adjust yourself to the sight of them."')
    wait()

    slow_print("After a while, you reach a house. You follow the monster inside, curious about what comes next.")
    wait()

    slow_print('"As a human living in the RUINS, monsters may attack you," she explains.')
    slow_print('"You will need to be prepared for this situation. However, worry not!"')
    slow_print('"The process is simple. When you encounter a monster, you will enter a FIGHT."')
    slow_print('"While you are in a FIGHT, strike up a friendly conversation. Stall for time. I will come to resolve the conflict."')
    slow_print('"Practice talking to the dummy first."')
    wait()
    slow_print("You approach the dummy cautiously.")
    slow_print("It stands there silently, unmoving, like a statue.")
    slow_print("You try to speak to it, but it makes no sound.")
    wait()
    slow_print("You look around, wondering if this is how the practice is supposed to start.")
    slow_print("The silence feels strange, but the monsters instructions echo in your mind.")
    wait()
    slow_print("After a while..")
    slow_print('"Ah, very good! You are very good," she praises warmly.')
    wait()
    slow_print("Finally, she leads you to a small resting room. She feeds you, bathes you, and takes care of every detail with gentle attention.")
    slow_print("The character feels an unfamiliar warmth and happiness, almost too good to be true.")
    wait()
    slow_print("She takes care of you, feeds you, hums lullabies.")
    slow_print("You feel so safe, so cared for, that you almost forget the darkness you came from.")
    wait()
    slow_print("But then, a thought pops into your head:")
    slow_print('"This can’t be real... I don’t deserve happiness."')
    slow_print("Fear and doubt claw at your mind.")
    wait()  
    slow_print("You decide to leave, to escape the comfort that feels too good to be true.")
    slow_print("As you reach the door, the monster’s demeanor shifts.")
    slow_print("She’s angry, almost like another personality has taken over.")
    slow_print('"You cannot go outside!" she shouts. "It’s dangerous out there!"')
    wait()

    slow_print("Her anger fades as quickly as it came, replaced by a softer, uneasy kindness.")
    slow_print('"I only want to keep you safe," she says gently.')
    slow_print("You feel uneasy but unable to resist her words completely.")
    wait()

    slow_print("She gestures toward the table: 'Dinner is ready. Go wash your hands.'")
    wait()
    slow_print("You eat together quietly, the warmth of the house contrasting with the heaviness of her warnings.")


    slow_print('"After dinner, it’s time to sleep," she says softly.')
    slow_print("You go to your room, lying down and thinking: *What was that?*")
    slow_print("Why did she react that way when you tried to leave?")
    wait()

    slow_print("Curiosity gnaws at you. What is outside? What could be out there?")
    slow_print("Late at night, you quietly sneak out, thinking she is asleep...")
    wait()
def mother_battle(player):
    slowprint("\nOne day, you find a door. The Mother shockingly appears in the door and, said as she speaks with a tone shifts when you touch it.")
    slowprint('"You must not go outside," she says. "It’s dangerous out there."')
    slowprint("Her voice trembles — half love, half fear.")
    
    spares = 0
    
    # List of progressive dialogue lines
    spare_lines = [
        "You whisper softly: 'I just want to understand.' Her hand trembles.",
        "\nHer tears fall. 'I only wanted to keep you safe. Why do you have to leave me?'",
        "\nHer face showed a fierce look. 'I gave you home to stay, how could you do this to me?'"
    ]
    
    while player.hp > 0:
        player.show_stats()
        slowprint("What do you do?")
        choice = prompt(["Attack", "Run", "Talk gently"])
        
        if choice == 0:
            slowprint("You attack. She blocks and hits you back effortlessly.")
            player.hp -= random.randint(2, 4)
            player.stress += 1
        elif choice == 1:
            slowprint("You try to flee — she grabs you by the arm. 'Don’t leave me!' she screams.")
            player.hp -= 1
            player.anxiety += 1
        else:
            spares += 1
            player.spare_counter += 1
            
            # Print the next line in the list if available
            if player.spare_counter <= len(spare_lines):
                slowprint(spare_lines[player.spare_counter - 1])
            else:
                # Once all lines are shown, repeat the last line or a closing message
                slowprint(spare_lines[-1])
            
            player.self_worth += 1
            
            # After 3 or more sparing actions, trigger the final choice
            if spares >= 3:
                slowprint("\nShe sighed softly, her expression turning gentle. 'Fine... just keep yourself safe, and remember what I taught you,' she said, a sad smile forming as pride glimmered in her eyes.")
                choice = prompt(["Stay", "Leave"])
                if choice == 0:
                    player.journal.append("Stayed with Mother")
                    return "stay"
                else:
                    player.journal.append("Left Mother")
                    return "leave"
    
    return "defeat"
# JOURNEY & NPC ENCOUNTERS
def journey_before_bosses(player):
    # Encounter Luma first
    talk_to_npc("Luma", player)
    slowprint("\nYou walk forward, the tall grass bending with the wind. Your heart feels light yet uneasy.")
    slowprint("Luma’s words echo in your mind: 'Joy is fragile, yet worth holding.'")
    wait()

    # Encounter Sage next
    slowprint("\nA faint, spirit-like figure drifts ahead, glowing softly. Its form is gentle yet ethereal, almost translucent.")
    slowprint("You feel an urge to approach, curiosity tinged with fear.")
    talk_to_npc("Sage", player)
    slowprint("\nAfter speaking with Sage, you continue your journey, each step stirring memories and questions you didn’t know you had.")
    wait()

    # Encounter Eon last
    talk_to_npc("Eon", player)
    slowprint("\nThe path stretches endlessly, twisting through strange tall grass. Shadows bend unnaturally, but you keep moving forward.")
    wait()
# INDIVIDUAL BOSS INTRODUCTIONS


# OUTSIDE JOURNEY
def outside_journey(player):
    slowprint("\nAs you step outside, the air feels different — crisp, alive, almost unreal.")
    slowprint("The sun filters through the leaves in strange, impossible patterns, painting the ground in colors you have never seen before.")
    slowprint("Your footsteps make no sound, yet every movement seems noticed, as if the forest itself is alive and watching.")
    wait()

    # Journey with NPCs and inner monologue
    journey_before_bosses(player)

    # Boss sequence with their intros
    mirror_of_doubt_intro(player)
    clock_of_pressure_intro(player)
    whispering_fog_intro(player)
    gray_king_intro(player)
    
    # Show final stats after all bosses
    player.show_stats()

    # NPC encounters before bosses
    npcs = ["Luma", "Sage", "Eon"]
    for _ in range(2):  # encounter 2 NPCs before bosses
        talk_to_npc(random.choice(npcs), player)

    # Define bosses and shuffle except the final boss
    bosses = [
        ("Mirror of Doubt", "self_sabotage"),
        ("Clock of Pressure", "stress"),
        ("Whispering Fog", "anxiety"),
        ("Gray King", "self_worth")
    ]
    random.shuffle(bosses[:-1])
    bosses.append(("Gray King", "self_worth"))

    # Begin boss encounters
    for boss, stat in bosses:
        slowprint(f"\nA new presence emerges ahead — {boss}. The air changes; tension coils like a living thing around you.")
        boss_puzzle(boss, stat, player)
        player.show_stats()
        
