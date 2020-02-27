from nba_py import game

boxscore_summary = game.BoxscoreSummary("0021800526")
print(boxscore_summary.game_summary())
print(boxscore_summary.other_stats())
print(boxscore_summary.officials())
