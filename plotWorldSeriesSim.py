# Monte Carlo Simulation of the likelihood that the better team wins a series of X games
#   if we know the team's chances of winning a single game

import numpy as np
import matplotlib.pyplot as plt


def plot_win_rate_vs_num_games_in_series(max_number_of_games_in_series, chance_better_team_wins=.60, num_trials=100):
    """Plots the win rate for the better team based on the number games in the series.
    Estimates win rates based on Monte Carlo simulation.
    Plotted number of games in series will be odd numbers between 3 and max_number_of_games_in_series.
    """
    series_win_rates = []
    list_of_num_games_in_series = range(3, max_number_of_games_in_series, 2)

    for num_games_in_series in list_of_num_games_in_series:
        series_win_rate = simulate_world_series(chance_better_team_wins, num_games_in_series, num_trials)
        series_win_rates.append(series_win_rate)

    plt.plot(list_of_num_games_in_series, series_win_rates)
    plt.xlabel("Number of Games in Series")
    plt.ylabel("Likelihood That the Better Team Wins the Series")
    plt.title(f"Series win rate, if X games, and the better team has a\n"
              f" {chance_better_team_wins*100}% chance of winning a single game")
    plt.show()


def simulate_world_series(chance_better_team_wins, num_games_in_series, num_trials):
    num_series_won_by_better_team = 0

    # 2D numpy array: num_rows=trials, num_cols=games in series
    outcomes_array = np.random.random(size=(num_trials, num_games_in_series))

    for series in outcomes_array:
        num_games_won_by_better_team = np.count_nonzero(series < chance_better_team_wins)
        if num_games_won_by_better_team > (num_games_in_series - num_games_won_by_better_team):
            num_series_won_by_better_team += 1

    series_win_rate = num_series_won_by_better_team / float(num_trials)
    return series_win_rate


upper_bound_num_games_in_series = 201
better_team_win_rate = .6
num_times_each_series_is_simulated = 300

plot_win_rate_vs_num_games_in_series(
    upper_bound_num_games_in_series,
    better_team_win_rate,
    num_times_each_series_is_simulated)
