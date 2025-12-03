from hogwarts.universe.house import assign_house
from hogwarts.utils.input_utils import ask_choice, init_character


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
        character["Attributes"]["loyalty"] += 1
    else: 
        print("Ron looks a bit disappointed but nods.\n")
        character["Attributes"]["ambition"] += 1

    print("A girl enters next, already carrying a stack of books.")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")

    choice = ask_choice(
        "How do you respond?",
        ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."]
    ) + 1

    if choice == 1:
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!\n")
        character["Attributes"]["intelligence"] += 1
    else:
        print("Hermione raises an eyebrow but smiles politely.\n")
        character["Attributes"]["courage"] += 1

    print("Then a blonde boy enters, looking arrogant.")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")

    choice = ask_choice(
        "How do you respond?",
        ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."]
    ) + 1

    if choice == 1:
        print("Draco smirks approvingly.\n")
        character["Attributes"]["ambition"] += 1
    elif choice == 2:
        print("Draco frowns, annoyed. — You'll regret that!\n")
        character["Attributes"]["loyalty"] += 1
    else: 
        print("Draco looks shocked by your boldness.\n")
        character["Attributes"]["courage"] += 1

    print("The train continues its journey. Hogwarts Castle appears on the horizon...\n")
    print("Your choices already say a lot about your personality!")
    print("Your updated attributes:", character["Attributes"])

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
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]

    answers = []

    for q_text, options, houses in questions:
        print(q_text)
        choice = ask_choice("Your choice:", options) + 1   # => 1, 2, 3 ou 4
        answers.append(choice)
        print()  # ligne vide pour lisibilité

    final_house = assign_house(character, questions)

    character["House"] = final_house

    print("The Sorting Hat exclaims:", final_house + "!!!")
    print("You join the students of " + final_house + " to loud cheers!\n")

fabio=init_character('Devine', 'Fabio', {'courage':8,'intelligence':8,'loyalty':8,'ambition':8})


