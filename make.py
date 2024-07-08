import json
import os

def main():
    cwd = os.getcwd()

    function = ""
    tick = ""

    with open(os.path.join(cwd, 'settings.json')) as f:
        settings = json.load(f)

        if settings["scoreboard"]:
            function += "scoreboard objectives setdisplay sidebar bac_advancements\n"

        if settings["hardcore"] or settings["terralith"]:
            function += "function blazeandcave:global_config\n"

        for reward in settings["rewards"]:
            status = settings["rewards"][reward]
            valid = ["on","off","first","first_team"]
            if status in valid:
                if status != "on":
                    function += f"function blazeandcave:config/{reward}_{status}\n"
            else:
                print(f"invalid option \"{status}\" given for {reward}, valid options include on, off, first, or first_team")
                exit()

        if settings["multiplayer"]["co-op"]:
            team = settings["multiplayer"]["team"]
            if team == "none":
                function +="function blazeandcave:config/coop_on\n"
                if settings["scoreboard"]:
                    print("*Warning*: Showing Scoreboard in non team co-op shows all players, it is recommended to set a team to display the scoreboard")
            else:
                valid = ["aqua","black","blue","dark_aqua","dark_blue","dark_gray","dark_green","dark_purple","dark_red","gold","gray","green","light_purple","red","white","yellow"]
                if team in valid:
                    function+="function blazeandcave:config/coop_on_team\n"
                    tick+=f"team join bac_team_{team} @a[team=!bac_team_{team}]"
                    if settings["scoreboard"]:
                        function+="scoreboard objectives setdisplay sidebar bac_advancements_team\n"
                else:
                    teams=""
                    for i in valid:
                        teams += i + " "
                    print(f"Invalid team color given, type 'none' or one of the following teams:\n{teams}")
                    exit()

    function +="\nscoreboard players set load settings_load 1"
    
    # Write Datapack for both 1.21+ and 1.20-
    for i in ["function","functions"]:
        with open(os.path.join(cwd,'BAC-Extra','data','bac_settings',i,'settings.mcfunction'),"w") as f:
            f.write(function)
        with open(os.path.join(cwd,'BAC-Extra','data','bac_settings',i,'tick.mcfunction'),"w") as f:
            f.write(tick)

    print("Done!")

        
main()