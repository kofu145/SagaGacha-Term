import sys
import consolemanager
import prompt_win
import gacha_win
import keygetter

def intro_method():
    manager = consolemanager.ConsoleManager()
    manager.resize(40, 130)
    manager.clear()
    manager.hide_cursor()
    prompt = prompt_win.Prompt(manager, ["Pokemon", "Abilities", "Items"])
    while True:
        choice_idx, choice = prompt.invoke()

        rarities = ["UR (Ultra Rare)|purple_4a", "SR (Super Rare)|light_goldenrod_1", "R (Rare)|light_cyan_3", "C (Common)|light_slate_grey"]
        odds = [5, 25, 30, 40]
        packs = [f"{choice} Pack - SGSS Saga"]
        gacha = gacha_win.GachaPrompt(manager, packs, rarities, odds, f"{choice.lower()}_pack.json", choice == "Pokemon")
        gacha.invoke()

        manager.clear()
        # if key == b'\r':
            

    sys.exit()

def test_box():
    manager = consolemanager.ConsoleManager()
    manager.clear()
    print(manager.boxed_text("Honchkrow\nAbility: Speed Boost\nEVs: 252 Atk / 252 Spe\nNaughty Nature\n- Brave Bird\n- Sucker Punch\n- Protect"))

if __name__ == "__main__":
    #test_box()
    intro_method()