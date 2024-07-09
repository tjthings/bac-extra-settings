scoreboard objectives add settings_load dummy

execute unless score load settings_load matches 1 run schedule function bac_settings:settings 1s