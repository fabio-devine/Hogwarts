import json
import random

from hogwarts.universe.house import update_house_points, display_winning_house
from hogwarts.utils.input_utils import load_file, init_character, display_character


def learn_spells(character,file_path="data/spells.json"):
    spells=load_file(file_path)
    utility_count,defensive_count,offensive_count=0,0,0
    learned_spells=[]
    while utility_count < 3 and defensive_count < 1 and offensive_count < 1:
        chosen=random.choice(spells)
        if chosen['type']=="Utility":
            utility_count+=1
        elif chosen['type']=="Defensive":
            defensive_count+=1
        else:
            offensive_count+=1
        learned_spells.append(chosen)
        spells.remove(chosen)
    while utility_count < 3:
        chosen=random.choice(spells)
        if chosen['type']=="Utility":
            utility_count+=1
            learned_spells.append(chosen)
            spells.remove(chosen)
    while defensive_count < 1 :
        chosen=random.choice(spells)
        if chosen['type']=="Defensive":
            defensive_count+=1
            learned_spells.append(chosen)
            spells.remove(chosen)
    while offensive_count < 1 :
        chosen=random.choice(spells)
        if chosen['type']=="Offensive":
            utility_count+=1
            learned_spells.append(chosen)
            spells.remove(chosen)
    print('You begin your magic lessons at Hogwarts...')
    for spell in learned_spells:
        print('You have just learned the spell: {} ({})'.format(spell['name'],spell['type']))
        input('Press Enter to continue...')
    print('')
    print('You have now completed your basic spell training at Hogwarts!\n Here are the spells you now master:')
    print('')
    for spell in learned_spells:
        print('- {:<} ({}) : {}'.format(spell['name'],spell['type'],spell['description']))
        character['Spells'].append(spell['name'])

def magic_quiz(character,file_path="data/magic_quiz.json"):
    questions=load_file(file_path)
    print('Welcome to your magic quiz ! \n Answer the 4 questions correctly to earn points for your house.')
    f_list=[]
    score=0
    while len(f_list)<4:
        question=random.choice(questions)
        if question not in f_list:
            f_list.append(question)
    for i in range(4):
        print('{}. {}'.format(i+1,f_list[i]['question']))
        an=input('>')
        if an ==f_list[i]['answer']:
            print('Correct answer! +25 points for your house')
            score+=25
        else:
            print('Wrong answer! The correct answer was : {}'.format(f_list[i]['answer']))
    print('Score obtained: {}'.format(score))
    return score

def start_chapter_3(character,houses):
    print("\n--- Chapter 3: Learning spells ---\n")
    learn_spells(character,file_path="data/spells.json")
    input('Press Enter to continue...')
    update_house_points(houses,character['House'],magic_quiz(character,file_path="data/magic_quiz.json"))
    input('Press Enter to continue...')
    display_winning_house(houses)
    input('Press Enter to continue...')
    display_character(character)

