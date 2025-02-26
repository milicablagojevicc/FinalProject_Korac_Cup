from Players import teams
import random
from datetime import datetime

def choose_team(teams):
    """
    Allows the user to choose a team out of the four qualified

    Args: teams: List of teams
    Returns: team: The chosen team
    Enumerate function used to label teams by number, make choosing easier
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
    Allows the user to choose 5 players from their chosen team

    Args: team: The team from which players are chosen
    Returns: list: List of 5 chosen players
    """
    print(f"\nChoose your starting five for {team.name}:")
    for i, player in enumerate(team.players, 1):
        print(f"{i}. {player.name} (Rating: {player.rating})")

    chosen_players = []
    while len(chosen_players) < 5:
        try:
            choice = int(input(f"Choose player {len(chosen_players) + 1} (enter the number): "))
            if 1 <= choice <= len(team.players) and team.players[choice - 1] not in chosen_players:
                chosen_players.append(team.players[choice - 1])
            else:
                print("Invalid number chosen / player already selected. Choose another number.")
        except ValueError:
            print("Please enter a valid number.")

    return chosen_players


def generate_player_stats(player):
    """
    Generates random stats for a player based on their rating (but reasonable within bounds of European basketball)

    Args: player: The player for which stats are generated
    Returns: dict: Dictionary containing the mian five player stats (Points, Rebounds, Assists, Steals, Blocks).
    """
    base = player.rating
    return {
        "Points": random.randint(max(0, base - 80), base - 60),
        "Rebounds": random.randint(max(0, base - 80), base - 70),
        "Assists": random.randint(max(0, base - 80), base - 70),
        "Steals": random.randint(0, max(1, (base - 50) // 10)),
        "Blocks": random.randint(0, max(1, (base - 50) // 10))
    }


def calculate_total_points(stats_list):
    """
    Calculates the total points scored by a team.

    Args: stats_list (list): List of dictionaries containing player stats.
    Returns: int: The total points scored by the team.
    """
    return sum(stats["Points"] for stats in stats_list)

def conduct_interviews(winner, loser, winner_stats, loser_stats):
    """
          Conducts post-game interviews with players from the winning and losing teams
          Args:
              winner (Team): The winning team
              loser (Team): The losing team
              winner_stats (list): List of dictionaries containing stats for each player in the winning team
              loser_stats (list): List of dictionaries containing stats for each player in the losing team
          Returns:
              None. Prints the interview responses to the console
          """
    print("\nPost-Game Interviews:")
    from Interviews import interview_responses

    winner_high_scorer = max(zip(winner.players, winner_stats), key=lambda x: x[1]["Points"])
    print(f"\n{winner_high_scorer[0].name} ({winner.name} - {winner_high_scorer[1]['Points']} points):")
    print(f'"{random.choice(interview_responses["winner"])}"')
    print(f'"{random.choice(interview_responses["high_scorer"])}"')

    # Interview losing team's player
    loser_interviewee = random.choice(list(zip(loser.players, loser_stats)))
    print(f"\n{loser_interviewee[0].name} ({loser.name} - {loser_interviewee[1]['Points']} points):")
    print(f'"{random.choice(interview_responses["loser"])}"')


def store_game_results(winner, loser, winner_stats, loser_stats):
    def store_game_results(winner, loser, winner_stats, loser_stats):
        """
        Stores the results of the game in a text file named 'game_results.txt'
        Args:
            winner (Team): The winning team
            loser (Team): The losing team
            winner_stats (list): List of dictionaries containing stats for each player in the winning team
            loser_stats (list): List of dictionaries containing stats for each player in the losing team

        Returns:
            None. Simply writes to a file and prints a confirmation message to the console
        """

    with open("game_results.txt", "a") as file:
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Winner: {winner.name}\n")
        file.write(f"Loser: {loser.name}\n")
        file.write(f"Score: {sum(player['Points'] for player in winner_stats)} - {sum(player['Points'] for player in loser_stats)}\n")
        file.write("Player Stats:\n")
        for team, stats in [(winner, winner_stats), (loser, loser_stats)]:
            file.write(f"{team.name}:\n")
            for player, stat in zip(team.players, stats):
                file.write(f"  {player.name}: {stat}\n")
        file.write("\n")
    print("Game results have been stored in 'game_results.txt'")

def main():
    """
    Main function to run the Korac Cup simulator:
    """
    print("Welcome to the Korac Cup Simulator!")

    team1 = choose_team(teams)
    remaining_teams = [team for team in teams if team != team1]
    team2 = choose_team(remaining_teams)

    players1 = choose_players(team1)
    players2 = choose_players(team2)

    print("\nPlayer Stats:")
    team1_stats = []
    team2_stats = []

    for team, players, stats_list in [(team1, players1, team1_stats), (team2, players2, team2_stats)]:
        print(f"\n{team.name}:")
        for player in players:
            stats = generate_player_stats(player)
            stats_list.append(stats)
            print(f"{player.name}: {stats}")

    team1_total = calculate_total_points(team1_stats)
    team2_total = calculate_total_points(team2_stats)

    print(f"\nTotal Points - {team1.name}: {team1_total}")
    print(f"Total Points - {team2.name}: {team2_total}")

    if team1_total > team2_total:
        winner, loser = team1, team2
        winner_stats, loser_stats = team1_stats, team2_stats
    else:
        winner, loser = team2, team1
        winner_stats, loser_stats = team2_stats, team1_stats

    print(f"\n{winner.name} wins!")

    conduct_interviews(winner, loser, winner_stats, loser_stats)
    store_game_results(winner, loser, winner_stats, loser_stats)

    print("Thanks for playing the Radivoje Korac Cup Simulator!")
    print("You can try to play again with different teams or players!")

