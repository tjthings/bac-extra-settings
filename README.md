# bac-standard-settings
 Generates a datapack to apply settings automatically to a world running Blaze and Caves Advancement Pack

# How to use
1) Download the source code from releases and unzip
2) Change what config settings you want to change in the settings.json file
3) Run make.py (python3 is required)
4) COPY (not move or cut) the BAC-Settings folder into your world's datapack folder

# Settings
scoreboard: true or false, whether to display the basic advancement scoreboard on the sidebar, becomes team scoreboard in team co-op
hardcore / terralith: true or false, runs the install functions for 
item, xp, trophy rewards: 
- "on" - reward enabled (default)
- "first" - reward only given to first player to get it
- "first_team" - first play in team (useless)
- "off" - turns off rewards

co-op: true or false, turns on co-op sharing mode
team - "none" by default, enabling a team adds all players to that team and shares advancements with the team. This is useful for showing a team advancement scoreboard on the sidebar rather than a list of individual players all with the same advancement count
VALID TEAM COLORS: aqua, black, blue, dark_aqua, dark_blue, dark_gray, dark_green, dark_purple, dark_red, gold, gray, green, light_purple, red, white, or yellow
