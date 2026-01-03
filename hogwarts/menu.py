from hogwarts.chapters.chapter_1 import start_chapter_1
from hogwarts.chapters.chapter_2 import start_chapter_2
from hogwarts.chapters.chapter_3 import start_chapter_3
from hogwarts.chapters.chapter_4 import start_chapter_4_quidditch
from hogwarts.chapters.chapter_5_extension import start_chapter_5


def display_main_menu():
    men=["Start Chapter 1 - Arrival in the magical world","Exit Game"]
    for i in range(2):
        print("{}. {}".format(i+1,men[i]))

def launch_main_choice():
    houses={
    "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
    "Ravenclaw":0
    }
    while True:
        display_main_menu()
        choice=int(input())
        if choice==1:
            break
        elif choice==2:
            exit('Goodbye')
        else:
            print("Invalid Choice")
    start_chapter_5(start_chapter_4_quidditch(start_chapter_3(start_chapter_2(start_chapter_1()),houses),houses))



