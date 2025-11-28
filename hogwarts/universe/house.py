from hogwarts.utils.input_utils import ask_choice

houses={
    "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
    "Ravenclaw":0
}

questions = [
    (
        "You see a friend in danger. What do you do?",
        ["Rush to help", "Think of a plan", "Seek help", "Stay calm "
"and observe"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "Which trait describes you best?",
        ["Brave and loyal", "Cunning and ambitious", "Patient and"
"hardworking", "Intelligent and curious"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),
    (
        "When faced with a difficult challenge, you...",
        ["Charge in without hesitation", "Look for the best"
"strategy", "Rely on your friends",
         "Analyze the problem"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    )
]

def update_house_points(houses,house_name,points):
    if house_name in houses:
        houses[house_name]+=points
        print('Points : ')
        for key in houses:
            print('{} : {}'.format(key,houses[key]))
    else:
        print("This house doesn't exist")

def display_winning_house(houses):
    max_points=0
    winner=[]
    for key in houses:
        if houses[key]>max_points:
            max_points=houses[key]
    for key in houses:
        if houses[key]==max_points:
            winner.append(key)
    print(','.join(winner))

def assign_house(character,questions):
    an=[]
    for question in questions:
        an.append(ask_choice(question[0],question[1]))
    l=[('Courage','Gryffindor'),('Ambition','Slytherin'),('Loyalty','Hufflepuff'),('Intelligence','Ravenclaw')]
    l2=[(0,'Gryffindor'),(1,'Slytherin'),(2,'Hufflepuff'),(3,'Ravenclaw')]
    for i in character:
        houses[l[i][1]]+=character[l[i][0]]*2
    for v in an:
        houses[l2[v][1]]+=3
