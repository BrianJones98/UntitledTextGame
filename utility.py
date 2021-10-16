from scenes import Scene
import commands

def await_command():
    print("Write Something: ", end='')
    return input().split()

def read_command(command, scene):
    if len(command) == 1 and command[0].lower() == "help":
        commands.display_help()
    elif(command == ["exit", "game"]):
        exit()
    elif("observe" in command):
        commands.observe(scene)
    else:
        print("Invalid Command")