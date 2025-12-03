from hogwarts.utils.input_utils import ask_text, ask_number, display_character, init_character, ask_choice, load_file


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
    print("")
    print('Catalog of available items :')
    data=load_file('../data/inventory.json')
    for key, value in data.items():
        n=value[0]
        p=value[1]
        print('{}. {} - {} Galleaons'.format(key,n,p),end='')
        if key=='1' or key=='2' or key=='4':
            print(' (required)')
        else:
            print('')
    print('')
    req = [data["1"][1], data["2"][1], data["4"][1]]
    while character["Money"]>0 and len(req)>=1:
        print('You have {} Galleaons.'.format(character["Money"]))
        print('Remaining required items : {}'.format(req))
        it=input("Enter the number of the item to buy : ")
        if character["Money"]<data[it][1]:
            exit('Sorry, you do not have enough money to buy this item.\n GAME OVER!')
        print('You bought : {} (-{} Galleaons)'.format(data[it][0],data[it][1]))
        print('')
    if len(req)>=1:
        exit('You are missing some required items...\n GAME OVER!')
    print('All required items have been purchased!')
    print('')
    print("It's time to choose your Hogwarts pet!")
    print('')
    print('You have {} Galleaons'.format(character["Money"]))
    print('')
    print('Available pets :')
    pets={"Owl":20,"Cat":15,"Rat":10,"Toad":10}
    i=1
    for key in pets:
       print("{}. {} - {} Galleaons".format(i,key,pets[key]))
       i=i+1
    pk=pets.keys()
    p=ask_choice('Which pet do you want to buy?',pk)
    if character["Money"]<pets[pk[p]]:
        exit('You do not have enough money to buy this pet! \n GAME OVER!')
    print('You chose: {} (-{} Galleaons)'.format(pk[p],pets[pk[p]]))

