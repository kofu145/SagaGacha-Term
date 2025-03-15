import json
from consolemanager import ConsoleManager, Transition
import sprite_rendering
import keygetter
import random


class GachaPrompt:
    def __init__(self, console_manager: ConsoleManager, pack_names: list[str], rarities: list[str], odds: list[int], data_file: str, mons=True, rolls=3):
        self.odds = odds
        self.rarities = rarities
        self.man = console_manager
        self.rolls = 3
        self.pack_names = pack_names
        self.render_mons = mons
        self.curr_choice = 0
        self.mon_rend = sprite_rendering.PokemonRenderer(console_manager)

        with open(data_file, "r") as f:
            self.data = json.load(f)

    def invoke(self):
        self.man.clear()

        x, y = self.man.get_cursor_pos()
        running = True
        while running:
            self.man.clear()
            self.prompt_screen()
            key = keygetter.getKey()
            if key in [b'd', "right"]:
                self.curr_choice = self.curr_choice + 1 if self.curr_choice + 1 < 2 else 1
            elif key in [b'a', "left"]:
                self.curr_choice = self.curr_choice - 1 if self.curr_choice - 1 > 0 else 0
            elif key == b'\r':
                if self.curr_choice == 0:
                    self.gacha(self.render_mons)
                elif self.curr_choice == 1:
                    running = False
            self.man.set_cursor(x, y)
        return

    def prompt_screen(self):

        self.man.banner(self.pack_names[0])

        r_rare = self.rarities[2].split("|")
        intro = f"{self.rolls} pulls per pack, last pull guarenteed {self.man.color_text(r_rare[0], None, r_rare[1])}"
        print(self.man.center_multiline_text(self.man.boxed_text(intro, 10, 0)), end="")

        colored_str = []
        for r in self.rarities:
            ts = r.split("|")
            colored_str.append(self.man.color_text(ts[0], None, ts[1]))
        odds_str = f"Odds for this pull:\n"
        for i in range(len(colored_str)):
            odds_str += f"{colored_str[i]}: {self.odds[i]}%"
            if i < len(colored_str) - 1:
                odds_str += "\n"
        
        if self.render_mons:
            odds_str = self.mon_rend.render_combined_text_arrs([self.mon_rend.get_sprite("chansey"), self.man.boxed_text(odds_str).split("\n")], 5, False).rstrip("\n")
            print(self.man.center_multiline_text(self.man.boxed_text(odds_str, 3)))
        else:
            print(self.man.center_multiline_text(self.man.boxed_text(odds_str, 3)))

        choices = ["Pull!", "Back"]
        promptstr = ""
        for i in range(len(choices)):
            bg = "none"
            fg = "none"
            if i == self.curr_choice:
                bg = "white"
                fg = "black"
            promptstr += self.man.color_text(choices[i], bg, fg) + "     "
        cent = self.man.center_multiline_text(self.man.boxed_text(promptstr.rstrip(), 5, 0))
        self.man.clear_curr_line()
        print(cent)


    def gacha(self, mons=False):
        for i in range(self.rolls):
            self.man.transition_clear(Transition.STRIPEDSIDEBYSIDE)
            self.man.set_cursor(1, 1)
            rarity = self.roll() if i < self.rolls - 1 else self.roll(True)
            choice_arr = self.data[self.rarities[rarity].split("|")[0][:2].rstrip()]
            fin = choice_arr[random.randint(0, len(choice_arr)-1)]
            ivstr = ""
            if mons:
                ivstr += "IVs: "
                ivtoguarentee = [6, 3, 1, 0]
                stats = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]
                guarenteed = []
                while len(guarenteed) < ivtoguarentee[rarity]:
                    new_number = random.randint(0, 5)
                    if new_number not in guarenteed:
                        guarenteed.append(new_number)
                for i in range(6):
                    iv = 31 if i in guarenteed else random.randint(0, 31)
                    ivstr += str(iv) + " " + stats[i]
                    if i < 5:
                        ivstr += " / "
                #l = fin.split("\n")
                #l.insert(2, ivstr)
                # fin = "\n".join(l)
            roll_str = fin
            sprite_name = fin.split("\n")[0].split("@")[0].rstrip()
            if mons:
                roll_str = self.mon_rend.render_combined_text_arrs([self.mon_rend.get_sprite(sprite_name.lower()), 
                                                                    self.man.boxed_text(fin).split("\n")], 5, False).rstrip("\n")
            self.man.banner("You received:")
            r_rare = self.rarities[rarity].split("|")
            intro = f"{self.man.color_text(r_rare[0], None, r_rare[1])}"
            print(self.man.center_multiline_text(self.man.boxed_text(intro, 15, 0)), end="")
            if mons:
                roll_str += "\n" + ivstr
            print(self.man.center_multiline_text(self.man.boxed_text(roll_str, 3)))
            
            print(self.man.center_multiline_text(self.man.boxed_text(self.man.color_text("Next", "white", "black").rstrip(), 5, 0)))
            l = fin.split("\n")
            l.insert(2, ivstr)
            fin = "\n".join(l)
            with open("pulls.txt", "a") as f:
                f.write(f"Pulled from {self.pack_names[0]}:\n")
                f.write(fin)
                f.write("\n\n")
            while True:
                key = keygetter.getKey()
                if key == b'\r':
                    break
        self.man.clear()
    
    def roll(self, guarentee=False):
        max_roll = 100
        if guarentee:
            max_roll = sum(self.odds[0:3])
        p = random.randint(1, max_roll)
        odd_sum = 0
        for i, odd in enumerate(self.odds):
            odd_sum += odd
            if p <= odd_sum:
                return i