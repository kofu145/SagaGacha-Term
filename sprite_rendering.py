from consolemanager import ConsoleManager

class PokemonRenderer:
    def __init__(self, console_manager: ConsoleManager):
        self.con_man = console_manager

    def get_sprite(self, pokemon, lines=True):
        with open(f"./sprites/regular/{pokemon}", "r", encoding="utf-8") as f:
            if lines:
                sprite = f.readlines()
            else:
                sprite = f.read()
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
        final = ""
        sprites = []
        for mon in pokemon_names:
            sprites.append(self.get_sprite(mon))
        
        max_height = max(len(sprite) for sprite in sprites)
        
        for i in range(len(sprites)):  # Normalize sprite heights
            max_width = max(len(self.con_man.cull_ansi(line)) for line in sprites[i]) 
            track_empty = " " * max_width
            if len(sprites[i]) < max_height and sprites[i][-1] == "[0m":
                sprites[i][-1] += track_empty
            while len(sprites[i]) < max_height:
                sprites[i].append(track_empty)  # Append only empty space, not duplicate content
        
        for i in range(max_height):
            combined = "".join(sprite[i].replace("\n", "") + " " * spacing for sprite in sprites)
            cent = self.con_man.center_text(combined)
            final += cent 
            if i < max_height:
                final += "\n"
        return final



    def render_combined_text_arrs(self, sprites: list[list[str]], spacing=2, centered=True):
        final = ""
        max_height = max(len(sprite) for sprite in sprites)
        
        for i in range(len(sprites)): 
            max_width = max(len(self.con_man.cull_ansi(line)) for line in sprites[i]) 
            track_empty = " " * max_width
            if len(sprites[i]) < max_height and sprites[i][-1] == "[0m":
                sprites[i][-1] += track_empty
            while len(sprites[i]) < max_height:
                sprites[i].append(track_empty)  
        
        for i in range(max_height):
            combined = "".join(sprite[i].replace("\n", "") + " " * spacing + "[0m" for sprite in sprites)
            cent = self.con_man.center_text(combined) if centered else combined
            
            final += cent 
            if i < max_height:
                final += "\n"
            
        return final