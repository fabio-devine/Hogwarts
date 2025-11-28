from hogwarts.utils.input_utils import ask_text, ask_number, display_character, init_character, ask_choice


def introduction():
    print('For as long as you can remember, something in your world has felt slightly \n'
          'out of place—like a note in a song that doesn’t quite match, or a shadow that \n'
          'moves just a little too quickly.')
    input('Press enter to continue...')
    print('Strange things happen around you sometimes: a light flickers when you’re upset, \n'
          'a book falls from a shelf at the perfect moment, \n'
          'a door unlocks when no one touches it. ')
    input('Press enter to continue...')
    print('People call them coincidences. You’re not so sure.Life carries on as usual, but \n'
          'lately there’s a tension in the air, a quiet hum beneath the ordinary. \n')
    input('Press enter to continue...')
    print('You feel it most in the early mornings, when the sun creeps\n'
          'across the floorboards, and in the late evenings, when the world seems to hold its breath.'
          'Something is coming. \n'
          'Something meant for you.\n'
          'And soon, your life will no longer be ordinary at all.')

def create_character():
    Last_name = ask_text("Enter your character's last name: ")
    First_name = ask_text("Enter your character's first name: ")
    print('')
    print('Choose your attributes: ')
    att={'Courage': 0, 'Intelligence': 0, 'Loyalty': 0, 'Ambition': 0}
    for key in att:
        att[key]=ask_number("{} level (1-10) : ".format(key),1,10)
    print('')
    print('Character profile: ')
    display_character(init_character(Last_name,First_name,att))

def receive_letter():
    print('An owl flies through the window, delivering a letter sealed with the '
          'Hogwarts crest...\n'
          '“Dear Student,\n'
          'We are pleased to inform you that you have been accepted to Hogwarts\n'
          'School of Witchcraft and Wizardry!”')
    print('')
    ch=ask_choice('Do you accept this invitation and go to Hogwarts?',['Yes, of course !',"No, I'd rather stay with Uncle Vernon..."])
    if ch==1:
        print('You tear up the letter, and Uncle Vernon cheers:\n'
              '“EXCELLENT! Finally, someone NORMAL in this house!”\n'
              'The magical world will never know you existed... Game over.')
        exit("Guess 'fun' isn't in your bucket list")

def meet_hagrid():
    print("Hagrid: 'Hello Harry! I’m here to help you with your shopping on Diagon Alley.'")
    ch=ask_choice('Do you want to follow Hagrid?',['Yes','No'])
    if ch==1:
        print('Hagrid gently insists and takes you along anyway!')

def buy_supplies(character):
    print('Welcome to Diagon Alley !')
