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

print(f"Total players: {len(players)}")
print(f"Matches array shape: {matches.shape}, dtype: {matches.dtype}")
print(f"Runs array shape: {runs.shape}, dtype: {runs.dtype}")
print(f"Wickets array shape: {wickets.shape}, dtype: {wickets.dtype}")
