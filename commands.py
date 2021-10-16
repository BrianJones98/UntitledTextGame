#General
def display_help():
    print("\n\n-----General Actions-----")
    print("help: will display this help menu if it is the only word typed")
    print("exit game: will exit the game (must be exact)")
    print("observe: observe your surroundings or an object/creature if one is present and specified")
    
    print("\n\n-----Diplomacy Actions-----")
    print("speak: speak with someone")

    print("\n\n-----Combat Actions-----")
    print("attack: attack something")

def observe(scene):
    climate = scene.climate

    print(f"The room you're in has a very {climate} climate")