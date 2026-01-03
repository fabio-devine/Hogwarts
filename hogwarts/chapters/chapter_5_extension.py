from hogwarts.utils.input_utils import ask_text, ask_number, display_character, init_character, ask_choice, load_file
from hogwarts.utils.input_utils import display_character, add_item, modify_money

def forest(character):
    print("\nYou enter the Forbidden Forest.")
    print("Giant spiders block your path!")
    courage = character["Attributes"]["Courage"]
    choice = ask_choice(
        "What do you do?",
        ["Use a spell", "Run away"]
    )
    if choice == 0:
        if courage >= 5:
            print("Your spell scares the spiders away!")
        else:
            print("Your spell is weak. You get bitten.")
            modify_money(character, -10)
    else:
        print("You flee in panic!")
        modify_money(character, -15)


def basilisk(character):
    print("\nYou enter the Chamber of Secrets.")
    print("The Basilisk appears!")
    courage = character["Attributes"]["Courage"]
    choice = ask_choice(
        "Choose your action:",
        ["Attack", "Look around"]
    )
    if choice == 1 and courage >= 6:
        print("You find the Sword of Gryffindor!")
        add_item(character, "Inventory", "Sword of Gryffindor")
    if "Sword of Gryffindor" in character["Inventory"]:
        print("You kill the Basilisk with the sword!")
    else:
        print("The Basilisk wounds you badly!")
        modify_money(character, -20)

def tom_riddle(character):
    print("\nTom Riddle appears.")
    intelligence = character["Attributes"]["Intelligence"]
    choice = ask_choice(
        "How do you react?",
        ["Destroy the diary", "Listen to him"]
    )
    if choice == 0 and intelligence >= 5:
        print("You destroy the diary. Tom Riddle disappears!")
        modify_money(character, 30)
    else:
        print("Tom Riddle manipulates you.")
        modify_money(character, -10)

def start_chapter_5(character):
    print("\n--- CHAPTER 5 : THE CHAMBER OF SECRETS ---")
    forest(character)
    basilisk(character)
    tom_riddle(character)

    print("\nThe adventure is over. Hogwarts is safe!")
    display_character(character)

