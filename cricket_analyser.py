"""
Cricket Player Stats Analyzer
Analyzes player batting and bowling stats using NumPy.
"""

import numpy as np

def load_data():
    """Returns player names and their stats as NumPy arrays."""

    # player names stored as python list
    players = ["Kohli", "Rohit", "De Villiers", "Root", "Smith", "Warner", "Williamson", "Bumrah", "Hazelwood", "Starc"]

    # stats stored as NumPy array
    matches = np.array([120, 115, 117, 130, 125, 110, 85, 95, 89, 100])
    runs = np.array([6200, 5800, 6000, 6700, 6100, 5200, 3100, 400, 800, 500])
    wickets = np.array([2, 1, 1, 3, 5, 4, 1, 180, 150, 200])

    print("Player Data".center(64))
    print("*" * 64)
    for i in range(len(players)):
        print(f"{players[i]:12s}  |  Matches: {matches[i]:4d}  |  Runs: {runs[i]:5d}  |  Wickets: {wickets[i]:3d}")
    print("*" * 64)
    print()

    # return players, matches, runs, wickets
    return players, matches, runs, wickets

def print_runs_and_wickets_stats(players, runs, wickets):
    """Prints average/max/min for runs and wickets, with player names."""
    
    # Runs statistics
    max_runs_player = players[np.argmax(runs)]
    min_runs_player = players[np.argmin(runs)]
    avg_runs = np.mean(runs)
    max_runs = np.max(runs)
    min_runs = np.min(runs)

    print("-" * 26)
    print("Run Statistics".center(26))
    print("-" * 26)
    print(f"Average Runs: {avg_runs}")
    print(f"Max Runs:     {max_runs} ({max_runs_player})")
    print(f"Min Runs:     {min_runs} ({min_runs_player})")
    print()

    # Wickets statistics
    max_wickets_player = players[np.argmax(wickets)]
    min_wickets_player = players[np.argmin(wickets)]
    avg_wickets = np.mean(wickets)
    max_wickets = np.max(wickets)
    min_wickets = np.min(wickets)

    print("-" * 28)
    print("Wicket Statistics".center(28))
    print("-" * 28)
    print(f"Average Wickets: {avg_wickets}")
    print(f"Max Wickets:     {max_wickets} ({max_wickets_player})")
    print(f"Min Wickets:     {min_wickets} ({min_wickets_player})")
    print()

def print_top_performers(players, runs, wickets):
    """Prints the top run-scorer and top wicket-taker."""

    # Top performers
    top_scorer_index = np.argmax(runs)
    top_scorer = players[top_scorer_index]

    top_wicket_index = np.argmax(wickets)
    top_wicket_taker = players[top_wicket_index]


    print("-" * 37)
    print("Top Performers".center(33))
    print("-" * 37)
    print(f"Top Run-Scorer:   {top_scorer} ({runs[top_scorer_index]} runs)")
    print(f"Top Wicket-Taker: {top_wicket_taker} ({wickets[top_wicket_index]} wickets)")
    print()

def print_batting_average(players, runs, matches):
    """Calculates and prints each player's batting average."""

    # Batting average per player (vectorized)
    # Dividing the whole 'runs' array by the whole 'matches' array at once,
    # NumPy does this element-by-element automatically; no loop needed
    batting_avg = runs / matches

    print("-" * 28)
    print("Batting Average per player".center(28))
    print("-" * 28)
    for i in range(len(players)):
        print(f"{players[i]:14s}:  {batting_avg[i]:>10.2f}")
    print()

def print_ranking(players, runs):
    """Ranks and prints players from highest to lowest runs."""
        
    # Ranking players by runs (highest to lowest)
    # np.argsort() gives indices that would sort the array smallest to largest
    # [::-1] reverses that order, so we get highest to lowest instead
    ranking_indices = np.argsort(runs)[::-1]

    print("-" * 30)
    print("Leaderboard (Ranked by Runs)".center(30))
    print("-" * 30)
    for rank, index in enumerate(ranking_indices, start=1):
        print(f"{rank:2d}. {players[index]:12s} -  {runs[index]} runs")
    print()

def print_players_above_threshold(players, runs, threshold=5000):
    """Filters and prints players above a given runs threshold."""

    # This creates a True/False array: one value per player, True if runs > threshold
    above_threshold = runs > threshold

    # Using that True/False array to select only the matching names and runs
    top_performers = np.array(players)[above_threshold]
    top_performers_runs = runs[above_threshold]

    print("-" * 34)
    print(f"Players with more than {threshold} runs".center(34))
    print("-" * 34)
    for name, r in zip(top_performers, top_performers_runs):
        print(f"{name:12s} - {r:>12} runs")

def main():
    players, matches, runs, wickets = load_data()
    print_runs_and_wickets_stats(players, runs, wickets)
    print_top_performers(players, runs, wickets)
    print_batting_average(players, runs, matches)
    print_ranking(players, runs)
    print_players_above_threshold(players, runs, threshold=5000)

if __name__ == "__main__":
    main()