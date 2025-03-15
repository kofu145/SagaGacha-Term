def render_combined_text_arrs(self, sprites: list[list[str]], spacing=0):
        if not sprites:
            return
        
        # Determine the max height of any sprite
        max_height = max(len(sprite) for sprite in sprites)
        
        # Normalize the height of all sprites
        for sprite in sprites:
            max_width = max(len(self.con_man.cull_ansi(line)) for line in sprite)
            while len(sprite) < max_height:
                sprite.append(" " * max_width)
        
        # Determine max width for each sprite
        sprite_widths = [max(len(self.con_man.cull_ansi(line)) for line in sprite) for sprite in sprites]
        
        # Construct and print each combined line
        for i in range(max_height):
            combined = "".join(sprite[i].ljust(sprite_widths[idx]) + (" " * spacing) for idx, sprite in enumerate(sprites))
            print(self.con_man.center_text(combined.rstrip()))


x = ["this is"]
y = [" blabla", "wahooey"]
print(render_combined_text_arrs([x, y]))