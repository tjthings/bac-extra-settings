import re
import os
import json

def main():
    data = os.path.join(os.getcwd(),'bacap_rewards','function')
    tags = os.path.join(os.getcwd(),'BAC-Extra', 'data', 'bacap_fanpacks','tags','function')
    dest = os.path.join(os.getcwd(),'BAC-Extra', 'data', 'bac_player_tracker','function')

    count = 0

    for tab in os.listdir(data):
        blacklist = ['exp', 'msg', 'trophy', 'reward', 'technical']
        if isFile(tab) or tab in blacklist: 
            continue    # ignore other reward folders and files

        for i in [tags, dest]:
            if not os.path.exists(os.path.join(i,tab)): 
                os.makedirs(os.path.join(i,tab))

        for func in os.listdir(os.path.join(data,tab)):
            count += 1
            name = os.path.splitext(func)[0] # Trim .mcfunction from filename

            with open(os.path.join(data,tab,func), "r") as f:
                content = f.read()
                # find internal adv name thru 'only' in adv grant
                adv = re.findall("(?<=only )(\S*)",content)[0]

                jsontag = {'replace': False, 'values':[f'bac_player_tracker:{tab}/{name}']}

                # Make JSON TAG
                with open(os.path.join(tags,tab,f'{name}.json'),"w") as f:
                    json.dump(jsontag,f,indent=4)

                mcfunction = f"execute unless score {adv} tracker_advancement matches 1.. run scoreboard players operation {adv} tracker_advancement = @s tracker_players"
                mcfunction += f"\nexecute unless score {adv} tracker_advancement_order matches 1.. run scoreboard players add .total tracker_advancement_order 1"
                mcfunction += f"\nexecute unless score {adv} tracker_advancement_order matches 1.. run scoreboard players operation {adv} tracker_advancement_order = .total tracker_advancement_order"

                # Make MCFUNCTION
                with open(os.path.join(dest,tab,func), "w") as output:
                    print(f"writing to {tab}/{func}")
                    output.write(mcfunction)
    
    # add_player runs from #bacap_fanpacks:bacap/root
    jsontag = {}
    with open (os.path.join(tags,'bacap','root.json'),"r") as f:
        jsontag = json.load(f)

    jsontag['values'].append('bac_player_tracker:add_player')

    with open (os.path.join(tags,'bacap','root.json'),"w") as f:
        json.dump(jsontag,f,indent=4)
    
    print(f'Wrote to {count} advancements')

def isFile(filename):
    return os.path.splitext(filename)[1] != '' # does filename have extension?

main()