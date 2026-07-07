"""
Cricket Player Stats Analyzer
Analyzes player batting and bowling stats using NumPy.
"""

import numpy as np

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

# Runs statistics
avg_runs = np.mean(runs)
max_runs = np.max(runs)
min_runs = np.min(runs)

print("Run Statistics".center(22))
print("-" * 23)
print(f"Average Runs: {avg_runs}")
print(f"Max Runs:     {max_runs}")
print(f"Min Runs:     {min_runs}")

print()

# Wickets statistics
avg_wickets = np.mean(wickets)
max_wickets = np.max(wickets)
min_wickets = np.min(wickets)

print("Wicket Statistics".center(22))
print("-" * 23)
print(f"Average Wickets: {avg_wickets}")
print(f"Max Wickets:     {max_wickets}")
print(f"Min Wickets:     {min_wickets}")

print()

# Top performers
top_scorer_index = np.argmax(runs)
top_scorer = players[top_scorer_index]

top_wicket_index = np.argmax(wickets)
top_wicket_taker = players[top_wicket_index]


print("Top Performers".center(33))
print("-" * 37)
print(f"Top Run-Scorer:   {top_scorer} ({runs[top_scorer_index]} runs)")
print(f"Top Wicket-Taker: {top_wicket_taker} ({wickets[top_wicket_index]} wickets)")