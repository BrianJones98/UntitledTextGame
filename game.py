import utility
import scenes

starting_scene = scenes.Scene("neutral")

while True:
    print("\n\nFlavor text goes here", end="\n\n")

    command = utility.await_command()
    utility.read_command(command, starting_scene)