from consolemanager import ConsoleManager

class PokemonRenderer:
    def __init__(self, console_manager: ConsoleManager):
        self.con_man = console_manager

    def get_sprite(self, pokemon):
        with open(f"./sprites/regular/{pokemon}", "r", encoding="utf-8") as f:
            sprite = f.readlines()
        return sprite

    def render_sprite(self, pokemon):
        sprite = self.get_sprite(pokemon)
        for line in sprite:
            cent = line.replace("\n", "")
            print(cent)

    def render_sprite_centered(self, pokemon):
        sprite = self.get_sprite(pokemon)
        for line in sprite:
            cent = self.con_man.center_text(line.replace("\n", ""))
            print(cent)
    
    def render_sprites_centered(self, pokemon_names: list[str], spacing=2):
        sprites = []
        for mon in pokemon_names:
            sprites.append(self.get_sprite(mon))
        
        max = 0
        max_idx = 0
        for i in range(len(sprites)):
            if len(sprites[i]) > max:
                max = len(sprites[i])
                max_idx = i
        width_offset = 0
        for i in range(len(sprites)):
            max_width = 0
            if i != max_idx and len(sprites[i]) < max:
                for k in range(len(sprites[i])):
                    if len(self.con_man.cull_ansi(sprites[i][k])) > max_width:
                        max_width = len(self.con_man.cull_ansi(sprites[i][k]))
                width_offset += max_width
                sprites[i][-1] += " " * max_width
                for j in range(max - len(sprites[i])):
                    sprites[i].append(sprites[i][-1])

        for i in range(max):
            combined = ""
            for sprite in sprites:
                combined += sprite[i].replace("\n", "") + " " * spacing
            cent = self.con_man.center_text(combined.replace("\n", ""))
            print(cent)

    