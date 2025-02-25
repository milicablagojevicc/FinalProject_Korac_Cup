def main():
    """
    Main function to run the basketball game simulator.
    """
    print("Welcome to the Basketball Game Simulator!")

    team1 = choose_team(teams)
    remaining_teams = [team for team in teams if team != team1]
    team2 = choose_team(remaining_teams)

    players1 = choose_players(team1)
    players2 = choose_players(team2)

    score1 = calculate_team_score(players1)
    score2 = calculate_team_score(players2)

    print(f"\n{team1.name} Score: {score1:.2f}")
    print(f"{team2.name} Score: {score2:.2f}")

    winner = team1 if score1 > score2 else team2
    loser = team2 if winner == team1 else team1
    print(f"\n{winner.name} wins!")

    print("\nPlayer Stats:")
    winner_stats = []
    loser_stats = []

    for team, players, stats_list in [(winner, players1, winner_stats), (loser, players2, loser_stats)]:
        print(f"\n{team.name}:")
        for player in players:
            stats = generate_player_stats(player)
            stats_list.append(stats)
            print(f"{player.name}: {stats}")

    # Ensure the winner has more total points
    winner_stats, loser_stats = ensure_higher_score(winner, loser, winner_stats, loser_stats)

    # Calculate and print total team scores
    winner_total = calculate_total_team_score(winner_stats)
    loser_total = calculate_total_team_score(loser_stats)
    print(f"\nTotal Score - {winner.name}: {winner_total}")
    print(f"Total Score - {loser.name}: {loser_total}")

    # Print adjusted stats if necessary
    if winner_stats != [generate_player_stats(player) for player in players1]:
        print("\nAdjusted Player Stats to Ensure Winner Has More Points:")
        for team, players, stats_list in [(winner, players1, winner_stats), (loser, players2, loser_stats)]:
            print(f"\n{team.name}:")
            for player, stats in zip(players, stats_list):
                print(f"{player.name}: {stats}")


if __name__ == "__main__":
    main()