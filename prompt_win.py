import sys
import consolemanager
import sprite_rendering
import keygetter

class Prompt:
    def __init__(self, console_manager : consolemanager.ConsoleManager, choices: list[str], default_sprite="ho-oh"):
        self.con_man = console_manager
        self.choices = choices
        self.default_sprite = default_sprite
        self.sprite_renderer = sprite_rendering.PokemonRenderer(console_manager)
        self.curr_choice = 0

    def invoke(self) -> str:
        x, y = self.con_man.get_cursor_pos()
        running = True
        while running:
            
            self.render()
            key = keygetter.getKey()
            if key in [b'd', "right"]:
                self.curr_choice = self.curr_choice + 1 if self.curr_choice + 1 < len(self.choices) else len(self.choices) - 1
            elif key in [b'a', "left"]:
                self.curr_choice = self.curr_choice - 1 if self.curr_choice - 1 > 0 else 0
            elif key == b'\r':
                running = False
            self.con_man.set_cursor(x, y)
        return (self.curr_choice, self.choices[self.curr_choice])


    def render(self):
        self.con_man.banner("Welcome to Kofu's custom SGSS pack simulator!")

        self.sprite_renderer.render_sprites_centered(["ho-oh", "lugia"], 5)
               
        promptstr = ""
        for i in range(len(self.choices)):
            bg = "none"
            fg = "none"
            if i == self.curr_choice:
                bg = "white"
                fg = "black"
            promptstr += self.con_man.color_text(self.choices[i], bg, fg) + " "
        cent = self.con_man.center_text(promptstr)
        self.con_man.clear_curr_line()
        print(cent)
        