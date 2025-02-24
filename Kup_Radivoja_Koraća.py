from Players import teams
import random

def choose_team(teams):
    print("Teams competing in the Radivoje Korac Cup:")
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team.name}")
    while True:
        try:
            choice = int(input("Choose a team (enter the number): "))
            if 1 <= choice <= len(teams):
                return teams[choice - 1]
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Please enter a valid number (between 1 and 12).")