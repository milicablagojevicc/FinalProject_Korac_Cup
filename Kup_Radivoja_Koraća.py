from Players import teams
import random

def choose_team(teams):
    """
    Allows the user to choose a team from the list of available teams.

    Args: teams (list): List of team objects.
    Returns: team: The chosen team object.
    """
    print("\nQualified teams:")
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team.name}")
    while True:
        try:
            choice = int(input("Choose a team (between 1 and 4): "))
            if 1 <= choice <= len(teams):
                return teams[choice - 1]
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Please enter a valid number.")


def choose_players(team):
    """
    Allows the user to choose 5 players from the selected team.

    Args:
        team: The team object from which players are chosen.

    Returns:
        list: List of 5 chosen player objects.
    """
    print(f"\nChoose 5 players for {team.name}:")
    for i, player in enumerate(team.players, 1):
        print(f"{i}. {player.name} (Rating: {player.rating})")

    chosen_players = []
    while len(chosen_players) < 5:
        try:
            choice = int(input(f"Choose player {len(chosen_players) + 1} (enter the number): "))
            if 1 <= choice <= len(team.players) and team.players[choice - 1] not in chosen_players:
                chosen_players.append(team.players[choice - 1])
            else:
                print("Invalid choice or player already selected. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    return chosen_players


def calculate_team_score(players):
    """
    Calculates the average rating of a team based on the chosen players.

    Args:
        players (list): List of player objects.

    Returns:
        float: The average rating of the team.
    """
    return sum(player.rating for player in players) / len(players)


def generate_player_stats(player):
    """
    Generates random stats for a player based on their rating.

    Args:
        player: The player object for which stats are generated.

    Returns:
        dict: Dictionary containing the player's stats (Points, Rebounds, Assists, Steals, Blocks).
    """
    base = player.rating
    return {
        "Points": random.randint(max(0, base - 20), base - 10),
        "Rebounds": random.randint(max(0, base - 40), base - 10),
        "Assists": random.randint(max(0, base - 40), base - 10),
        "Steals": random.randint(0, max(1, (base - 50) // 10)),
        "Blocks": random.randint(0, max(1, (base - 50) // 10))
    }


def calculate_total_team_score(player_stats):
    """
    Calculates the total score of a team based on player stats.

    Args:
        player_stats (list): List of dictionaries containing player stats.

    Returns:
        int: The total score of the team.
    """
    return sum(sum(stats.values()) for stats in player_stats)


def ensure_higher_score(winner, loser, winner_stats, loser_stats):
    """
    Ensures that the winning team has more total points than the losing team.

    Args:
        winner: The winning team.
        loser: The losing team.
        winner_stats (list): List of stats for the winning team's players.
        loser_stats (list): List of stats for the losing team's players.

    Returns:
        tuple: Tuple containing the adjusted stats for both teams.
    """
    winner_total = sum(sum(stats.values()) for stats in winner_stats)
    loser_total = sum(sum(stats.values()) for stats in loser_stats)

    if winner_total <= loser_total:
        adjustment = loser_total - winner_total + 1
    else