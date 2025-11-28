import json

def ask_text(text):
    return input(text).strip()

def ask_number(message,min=None,max=None):
    while True:
        number = int(input(message))
        if min <= number <= max:
            return number
        print('Please enter a number between {} and {}'.format(min,max))

def ask_choice(message,options):
    print(message)
    for i in range(len(options)):
        print('{}.'.format(i+1),options[i])
    choice = int(input('Your choice : '))
    return choice-1

def load_file(file_path):
    with open(file_path,'r', encoding='utf-8') as f:
        return json.load(f)

def init_character(last_name, first_name, attributes):
    player={"Last Name":last_name,"First Name":first_name,"Money":100,"Inventory":[],"Spells":[],"Attributes":attributes}
    return player

def display_character(character):
    for key in character:
        if type(character[key]) == dict:
            print(key, ':')
            for subkey in character[key]:
                print('- {} : {}'.format(subkey,character[key][subkey]))
        elif type(character[key]) == list:
            l=','.join(character[key])
            print(key, ':', l)
        else :
            print(key, ':', character[key])

def modify_money(character,amount):
    character['Money']+=amount

def add_item(character, key, item):
    if key=='Inventory' or key=='Spells':
        character[key].append(item)

