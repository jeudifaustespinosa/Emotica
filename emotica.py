import sys, time, random, textwrap
from texthelper import slowprint, slow_print, wait, prompt
from characters import Player, talk_to_npc
from bosses import boss_puzzle, mirror_of_doubt_intro, clock_of_pressure_intro, whispering_fog_intro, gray_king_intro
from story import cinematic_intro, mother_battle, journey_before_bosses, outside_journey
from endings import determine_ending, ending_scene




def main():
    slowprint("✨ Welcome to EMOTICA ✨")
    name = input("What is your name, dreamer? > ").strip() or "Wanderer"
    player = Player(name)
    cinematic_intro(player)
    result = mother_battle(player)
    if result == "leave":
        outside_journey(player)
    outcome = determine_ending(player, result)
    ending_scene(outcome, player)

if __name__ == "__main__":
    main()
