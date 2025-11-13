import random
import time
from texthelper import slowprint, slow_print, wait, prompt

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.stress = 5
        self.anxiety = 5
        self.self_sabotage = 5
        self.self_worth = 3
        self.relationships = {"Luma": 0, "Sage": 0, "Eon": 0}
        self.journal = []
        self.spare_counter = 0
    def show_stats(self):
        print(f"\n❤️ HP:{self.hp} | 😰 Stress:{self.stress} | 🌫️ Anxiety:{self.anxiety} | 💀 Self-Sabotage:{self.self_sabotage} | 🌱 Self-Worth:{self.self_worth}\n")


def talk_to_npc(npc, player):
    if npc == "Luma":
        slowprint("You meet Luma — a bright, soft-spoken girl with glowing eyes. She asks gently,")
        slowprint(f'"{player.name}, do you ever feel like joy is too fragile to hold?"')
        choice = prompt(["Agree quietly", "Say joy is worth holding anyway", "Change the subject"])
        if choice == 0:
            slowprint("Luma nods sadly. You both sit in silence. Something unspoken connects you.")
            player.relationships["Luma"] += 1
            player.anxiety -= 1
        elif choice == 1:
            slowprint("She smiles faintly. 'Maybe you’re right. Maybe that’s brave of you.'")
            player.relationships["Luma"] += 2
            player.self_worth += 1
        else:
            slowprint("She tilts her head. 'You don’t like deep talks, huh?'")
            player.relationships["Luma"] -= 1
            player.stress += 1
        player.journal.append("Talked to Luma")
    elif npc == "Sage":
        slowprint("\nYou find Sage meditating beneath a clocktower draped in living vines, its gears turning with the rhythm of unseen time.")
        slowprint("\nThe world beyond is dreamlike — yet painfully honest. The sky hums softly, and you feel your emotions begin to take shape around you.")
        slowprint('\nSage opens their eyes slowly, the glow of understanding flickering within them.')
        slowprint('"Everything is loud here," they whisper, voice trembling like wind over broken glass. "Even our thoughts echo until they hurt."')
        slowprint('"Out there, silence hides the truth. But here—" they pause, looking past you, as if seeing through your soul. "Here, every scream, every memory, every regret takes form."')
        slowprint('"Tell me... when your own mind begins to scream back at you, will you listen, or will you run?"')     
        choice = prompt(["Breathe slowly", "Distract yourself", "Scream louder"])
        slowprint("")
        if choice == 0:
            slowprint('"Good. You listened," Sage says. The vines calm down.')
            player.relationships["Sage"] += 2
            player.stress -= 2
        elif choice == 1:
            slowprint('"Escape has its place. But the noise always returns," Sage murmurs.')
            player.relationships["Sage"] += 1
            player.anxiety -= 1
        else:
            slowprint('"Then you meet the scream head-on," Sage says, impressed.')
            player.relationships["Sage"] += 1
            player.self_sabotage -= 1
        player.journal.append("Talked to Sage")
    elif npc == "Eon":
        slowprint("Eon is a traveler in a tattered red scarf. He seems to know your face.")
        slowprint('"You look like someone who’s tired of running," he says. "Why not rest?"')
        choice = prompt(["Sit beside him", "Say you can’t stop now", "Ignore him"])
        if choice == 0:
            slowprint('"Good," Eon whispers. "Even heroes need pauses."')
            player.relationships["Eon"] += 2
            player.stress -= 1
        elif choice == 1:
            slowprint('"Then don’t stop. Just promise to look at the stars once in a while," he grins.')
            player.relationships["Eon"] += 1
            player.self_worth += 1
        else:
            slowprint("He shrugs, his eyes dimming a bit.")
            player.relationships["Eon"] -= 1
            player.anxiety += 1
        player.journal.append("Talked to Eon")

