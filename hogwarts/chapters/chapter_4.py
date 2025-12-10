from hogwarts.utils.input_utils import ask_text, load_file, display_character


def randint(a, b):
    import random
    return random.randint(a, b)


def create_team(house, team_data, is_player=False, player=None):
    players = []
    for member in team_data[house]:
        name = member["name"]
        role = member["role"]
        if is_player and role == "Seeker" and player is not None:
            name = player
        players.append(f"{name} ({role})")

    return {
        "name": house,
        "score": 0,
        "goals_scored": 0,
        "goals_blocked": 0,
        "caught_snitch": False,
        "players": players
    }


def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance = randint(1, 10)

    if chance >= 6:
        if player_is_seeker:
            scorer = attacking_team["players"][0]
        else:
            scorer = attacking_team["players"][randint(0, len(attacking_team["players"]) - 1)]

        print(scorer, "scores a goal for", attacking_team["name"], "!(+10 points)")
        attacking_team["score"] += 10
        attacking_team["goals_scored"] += 1
    else:
        print(defending_team["name"], "blocks the attack!")
        defending_team["goals_blocked"] += 1


def golden_snitch_appears():
    x = randint(1, 6)
    return x == 6


def catch_golden_snitch(e1, e2):
    if randint(1, 2) == 1:
        winner = e1
    else:
        winner = e2

    winner["score"] += 150
    winner["caught_snitch"] = True
    print("The Golden Snitch has been caught by", winner["name"], "!(+150 points)")
    return winner


def display_score(e1, e2):
    print("Current score:")
    print("→", e1["name"] + ":", e1["score"], "points")
    print("→", e2["name"] + ":", e2["score"], "points")


def display_team(house, team):
    print(house, "team:")
    for p in team["players"]:
        print("-", p)


def quidditch_match(character, houses):
    team_data = load_file("../data/teams_quidditch.json")

    player_house = character["House"]
    available = []
    for h in team_data:
        if h != player_house:
            available.append(h)

    opponent = available[randint(0, len(available) - 1)]

    e1 = create_team(player_house, team_data, True, character["First Name"])
    e2 = create_team(opponent, team_data)

    print("Quidditch Match:", e1["name"], "vs", e2["name"])

    display_team(e1["name"], e1)
    display_team(e2["name"], e2)

    print("You are playing for", e1["name"], "as the Seeker")

    turn = 1
    while turn <= 20:
        print("Turn", turn)

        attempt_goal(e1, e2, True)
        attempt_goal(e2, e1, False)

        if golden_snitch_appears():
            winner = catch_golden_snitch(e1, e2)
            break

        display_score(e1, e2)
        ask_text("Press Enter to continue")

        turn += 1
    else:
        if e1["score"] > e2["score"]:
            winner = e1
        elif e2["score"] > e1["score"]:
            winner = e2
        else:
            winner = None

    display_score(e1, e2)

    if winner is None:
        print("Final result: Draw!")
    else:
        print("Final result:", winner["name"], "wins the match!")
        houses[winner["name"]] += 500
        print("+500 points for", winner["name"])

def start_chapter_4_quidditch(character, houses):
    print("--- Chapter 4: Quidditch ---")
    quidditch_match(character, houses)
    print("End of Chapter 4 — What an incredible performance on the field!")
    best = ""
    best_score = -99999
    for h in houses:
        if houses[h] > best_score:
            best_score = houses[h]
            best = h
    print("The winning house is", best, "with", houses[best], "points!")
    display_character(character)

