# Assigns a unique score to each player
# This runs when a player gets bacap root advancement
scoreboard players add .total tracker_players 1
scoreboard players operation @s tracker_players = .total tracker_players