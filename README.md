# Cricket Player Stats Analyzer

A beginner-friendly NumPy project that analyzes cricket player statistics — batting averages, top performers, rankings, and filtering — without using pandas.

## What it does

- Stores player stats (matches, runs, wickets) as NumPy arrays
- Calculates average, max, and min runs/wickets, showing which player holds each record
- Return the top performers
- Computes each player's batting average using vectorized division
- Ranks all players from highest to lowest runs
- Filters players above a chosen runs threshold

## How to run

1. Install the dependency:
   ```
   pip install -r requirements.txt
   ```
2. Run the script:
   ```
   python cricket_analyzer.py
   ```

## Sample output

```
Leaderboard (Ranked by Runs)
------------------------------
 1. Root       - 6700 runs
 2. Virat      - 6200 runs
 3. Smith      - 6100 runs
 ...
```

## What I learned

This project was built to practice core NumPy concepts: array creation, aggregate functions (`mean`, `max`, `min`), vectorized math, `argmax`/`argmin`, `argsort`, and boolean masking — all without relying on pandas.