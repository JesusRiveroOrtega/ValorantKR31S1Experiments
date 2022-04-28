# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt

number_games = 1000
number_trys = 10000
points = np.zeros((1, number_trys))
rank = np.zeros((1, number_trys))
rank_each_game = np.zeros((number_games, number_trys))

points_earned_mean = 0
points_earned_std = 10

for games in range(number_games):
    points_earned_current_game = np.round(np.random.normal(loc = points_earned_mean, scale = points_earned_std, size=number_trys))
    points += points_earned_current_game
    
    points_rank_decreasing_indexes = np.argwhere(points < 0)
    points_rank_increasing_indexes = np.argwhere(points > 100)
    
    
    if points_rank_decreasing_indexes.size != 0:
        for points_rank_decreasing_index in points_rank_decreasing_indexes:
            points[points_rank_decreasing_index[0], points_rank_decreasing_index[1]] = 50
            rank[points_rank_decreasing_index[0], points_rank_decreasing_index[1]] -= 1
            rank[points_rank_decreasing_index[0], points_rank_decreasing_index[1]] = rank[points_rank_decreasing_index[0], points_rank_decreasing_index[1]]*(rank[points_rank_decreasing_index[0], points_rank_decreasing_index[1]]>=0) 
        
    if points_rank_increasing_indexes.size != 0:
        for points_rank_increasing_index in points_rank_increasing_indexes:
            if rank[points_rank_increasing_index[0], points_rank_increasing_index[1]] == 22:
                pass
            else:
                points[points_rank_increasing_index[0], points_rank_increasing_index[1]] = 50
            rank[points_rank_increasing_index[0], points_rank_increasing_index[1]] += 1
    
    rank_each_game[games, :] = rank
    
average_rank_along_trys = np.average(rank_each_game, axis = 1)
std_rank_along_trys = np.average(rank_each_game, axis = 1)
    
plt.figure(1)
plt.plot(rank_each_game)
plt.figure(2)
plt.plot(average_rank_along_trys, color="k")
plt.plot(average_rank_along_trys - std_rank_along_trys, color="m")
plt.plot(average_rank_along_trys + std_rank_along_trys, color="m")
plt.figure(3)
s = (np.random.normal(loc = points_earned_mean, scale = points_earned_std, size=number_trys))
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(points_earned_std * np.sqrt(2 * np.pi)) * np.exp( - (bins - points_earned_mean)**2 / (2 * points_earned_std**2) ), linewidth=2, color='r')
plt.show()
