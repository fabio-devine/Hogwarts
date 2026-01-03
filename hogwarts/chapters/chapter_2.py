from hogwarts.chapters.chapter_1 import start_chapter_1
from hogwarts.universe.house import assign_house
from hogwarts.utils.input_utils import ask_choice, ask_text, load_file, display_character

def meet_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward...\n")
    print("A red-haired boy enters your compartment, looking friendly.")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you?")
    choice = ask_choice(
        "How do you respond?",
        ["Sure, have a seat!", "Sorry, I prefer to travel alone."]
    ) + 1
    if choice == 1:
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!\n")
        character["Attributes"]["Loyalty"] += 1
    else:
        print("Ron looks a bit disappointed but nods.\n")
        character["Attributes"]["Ambition"] += 1
    print("A girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    choice = ask_choice(
        "How do you respond?",
        ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."]
    ) + 1
    if choice == 1:
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!\n")
        character["Attributes"]["Intelligence"] += 1
    else:
        print("Hermione raises an eyebrow but smiles politely.\n")
        character["Attributes"]["Courage"] += 1
    print("Then a blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    choice = ask_choice(
        "How do you respond?",
        ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."]
    ) + 1

    if choice == 1:
        print("Draco smirks approvingly.\n")
        character["Attributes"]["Ambition"] += 1
    elif choice == 2:
        print("Draco frowns, annoyed. — You'll regret that!\n")
        character["Attributes"]["Loyalty"] += 1
    else:
        print("Draco looks shocked by your boldness.\n")
        character["Attributes"]["Courage"] += 1

    print("The train continues its journey. Hogwarts Castle appears on the horizon...\n")
    print("Your choices already say a lot about your personality!")
    print("Your updated attributes:", character["Attributes"])

def welcome_message():
    print("\nProfessor Dumbledore smiles at you.")
    print("Welcome to Hogwarts. I hope you will enjoy your time here.\n")


def sorting_ceremony(character):
    print("The sorting ceremony begins in the Great Hall...")
    print("The Sorting Hat observes you for a long time before asking its questions:\n")

    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends",
             "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]

    answers = []


    final_house = assign_house(character, questions)

    character["House"] = final_house

    print("The Sorting Hat exclaims:", final_house, "!!!")
    print("You join the students of ",final_house," to loud cheers!\n")

def enter_common_room(character):
    houses = load_file("data/houses.json")
    house_name = character["House"]
    info = houses[house_name]
    print("You follow the prefects through the castle corridors...\n")
    print(info['emoji'],info["description"])
    print()
    print(info["installation_message"])
    print("Your house colors:", ", ".join(info["colors"]))
    print()

def start_chapter_2(character):
    print("\n--- Chapter 2: Journey to Hogwarts ---\n")
    meet_friends(character)
    ask_text("\nPress Enter to continue...\n")
    welcome_message()
    ask_text("\nPress Enter to continue...\n")
    sorting_ceremony(character)
    ask_text("\nPress Enter to continue...\n")
    enter_common_room(character)
    ask_text("\nPress Enter to continue...\n")
    display_character(character)
    print("\nEnd of Chapter 2! Classes will begin soon at Hogwarts...\n")
    return character

