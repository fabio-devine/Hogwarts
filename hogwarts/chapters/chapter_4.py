from hogwarts.utils.input_utils import ask_text, ask_choice, load_file, modify_money
import random


def create_team(house, team_data, is_player=False, player=None):
    data = team_data[house]
    team = []

    for member in data:
        name = member["name"]
        role = member["role"]
        points = member["points"]

        if is_player and role == "Seeker" and player is not None:
            name = player

        team.append({"name": name, "role": role, "points": points})

    return team


def attempt_goal(player_is_seeker=False):
    choices = ["Try to score", "Pass to a teammate", "Try a risky move"]
    choice = ask_choice("Your action:", choices) + 1

    if player_is_seeker:
        if choice == 3:
            ask_text("You try a very risky dive! Press Enter...")
            return 20
        else:
            ask_text("You keep your eyes on the Snitch. Press Enter...")
            return 10

    if choice == 1:
        ask_text("You aim at the goal! Press Enter...")
        return 10
    elif choice == 2:
        ask_text("Good pass! Press Enter...")
        return 5
    else:
        ask_text("Risky move! Press Enter...")
        return 15


def golden_snitch_appears():
    x = random.randint(1, 6)
    return x == 6


def catch_golden_snitch(e1, e2):
    winner = random.choice([e1, e2])
    winner["score"] += 150
    winner["caught_snitch"] = True
    return winner


def display_score(e1, e2):
    print(e1["name"], ":", e1["score"])
    print(e2["name"], ":", e2["score"])


def play_turn(e1, e2, player_team, player_is_seeker=False):
    if golden_snitch_appears():
        winner = catch_golden_snitch(e1, e2)
        return winner

    if e1["team"] == player_team:
        points = attempt_goal(player_is_seeker)
        e1["score"] += points
    else:
        points = attempt_goal(False)
        e2["score"] += points

    return None


def play_match(e1, e2, player_team, player_is_seeker=False):
    e1["score"] = 0
    e2["score"] = 0
    e1["caught_snitch"] = False
    e2["caught_snitch"] = False

    while True:
        winner = play_turn(e1, e2, player_team, player_is_seeker)
        if winner is not None:
            return winner


def display_winner(winner):
    print(winner["name"], "wins the match with", winner["score"], "points!")


def start_chapter_4(character):
    print("\n--- Chapter 4: Quidditch ---\n")

    teams = load_file("../data/quidditch.json")

    house = character["House"]
    player = character["First Name"]

    player_team = create_team(house, teams, True, player)
    opponent_house = [h for h in teams if h != house][0]
    opponent_team = create_team(opponent_house, teams)

    e1 = {"name": house, "team": player_team, "score": 0}
    e2 = {"name": opponent_house, "team": opponent_team, "score": 0}

    winner = play_match(e1, e2, e1, True)

    display_score(e1, e2)
    display_winner(winner)

    modify_money(character, 30)

    ask_text("Press Enter to continue...")

    return character
