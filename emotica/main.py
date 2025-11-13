import sys, time, random, textwrap
import random
from texthelper import slowprint, slow_print, wait, prompt
from characters import Player, talk_to_npc
from bosses import boss_puzzle, mirror_of_doubt_intro, clock_of_pressure_intro, whispering_fog_intro, gray_king_intro
from story import cinematic_intro, mother_battle, journey_before_bosses, outside_journey
from endings import determine_ending, ending_scene, game_over



def main():
    """Main game loop — runs the game once, then asks whether to restart."""
    while True:
        slowprint("✨ Welcome to EMOTICA ✨")
        name = input("What is your name, dreamer? > ").strip() or "Wanderer"
        player = Player(name)

        cinematic_intro(player)
        result = mother_battle(player)
        if result == "leave":
            outside_journey(player)
        outcome = determine_ending(player, result)
        ending_scene(outcome, player)

        # After the ending, ask if player wants to restart
        while True:
            answer = input("\nDo you want to start again? (Y/N): ").strip().lower()
            if answer == "y":

                slow_print("\n...\n", 0.02)
                slow_print("🌙 A faint light flickers in the dark...", 0.02)
                wait()
                slowprint('"You came back..."', 0.03)
                break

            elif answer == "n":
                slow_print("\nThank you for playing EMOTICA. 🌹", 0.02)
                sys.exit()
            else:
                print("Please type Y or N.")
        

if __name__ == "__main__":
    main()
