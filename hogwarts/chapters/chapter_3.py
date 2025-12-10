import json
import random

from hogwarts.utils.input_utils import load_file, init_character


def learn_spells(character,file_path="../data/spells.json"):
    spells=load_file(file_path)
    utility_count,defensive_count,offensive_count=0,0,0
    while utility_count < 3 and defensive_count < 1 and offensive_count < 1:
        chosen=random.choice(spells)
        if chosen['type']=="Utility":
            utility_count+=1
        elif chosen['type']=="Defensive":
            defensive_count+=1
        else:
            offensive_count+=1
        character['Spells'].append(chosen)
        spells.remove(chosen)
    while utility_count < 3:
        chosen=random.choice(spells)
        if chosen['type']=="Utility":
            utility_count+=1
            character['Spells'].append(chosen)
            spells.remove(chosen)
    while defensive_count < 1 :
        chosen=random.choice(spells)
        if chosen['type']=="Defensive":
            defensive_count+=1
            character['Spells'].append(chosen)
            spells.remove(chosen)
    while offensive_count < 1 :
        chosen=random.choice(spells)
        if chosen['type']=="Utility":
            utility_count+=1
            character['Spells'].append(chosen)
            spells.remove(chosen)
    print('You begin your magic lessons at Hogwarts...')
    for spell in character['Spells']:
        print('You have just learned the spell: {} ({})'.format(spell['name'],spell['type']))
        input('Press Enter to continue...')
    print('')
    print('You have now completed your basic spell training at Hogwarts!\n Here are the spells you now master:')
    print('')
    for spell in character['Spells']:
        print('- {:<} ({}) : {}'.format(spell['name'],spell['type'],spell['description']))

def magic_quiz(character,file_path="../data/magic_quiz.json"):
    questions=load_file(file_path)
    for i in range(4):
