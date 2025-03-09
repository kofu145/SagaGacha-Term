import sys
import consolemanager
import prompt_win
import signal

def intro_method():
    print("Which pack to open?")
    manager = consolemanager.ConsoleManager()
    manager.clear()
    manager.hide_cursor()
    prompt = prompt_win.Prompt(manager, ["Pokemon", "Abilities", "Moves"])
    prompt.invoke()

    sys.exit()

if __name__ == "__main__":

    intro_method()