import re
import os

def main():
    data = os.path.join(os.getcwd(),'bc_rewards','function')
    dest = os.path.join(os.getcwd(), 'BAC-Extra', 'data', 'bc_rewards','function')

    for tab in os.listdir(data):
        for func in os.listdir(os.path.join(data,tab)):
            adv = ""
            with open(os.path.join(data,tab,func), "r") as f:
                content = f.read()
                # find internal adv name thru 'only' in adv grant
                adv = re.findall("(?<=only )(\S*)",content)[0]
                newline = f"execute unless score {adv} bac_obtained matches 1.. run scoreboard players operation {adv} tracker_advancement = @s tracker_players"
                with open(os.path.join(dest,tab,func), "w") as output:
                    print(f"writing to {tab}/{func}")
                    output.write(f'#NEW\n{newline}\n\n{content}')


main()