tellraw @s {"text":"                                             ","color":"dark_gray","strikethrough":true}

tellraw @s {"text":"Rare Animals","bold":true,"underlined":true,"color":"white"}
tellraw @s ["",{"text":"Axolotls Bred: ","color":"aqua"},{"score":{"name":"@s","objective":"stats_axolotls_bred"},"bold":true,"color":"aqua"}]
tellraw @s ["",{"text":"Pandas Bred: ","color":"white"},{"score":{"name":"@s","objective":"stats_pandas_bred"},"bold":true,"color":"white"}]
tellraw @s ["",{"text":"Llamas Tamed: ","color":"#F3DDB4"},{"score":{"name":"@s","objective":"stats_llamas_tamed"},"bold":true,"color":"#F3DDB4"}]

tellraw @s {"color":"gray","italic":true,"text":""}

tellraw @s {"text":"Chests","bold":true,"underlined":true,"color":"white"}
tellraw @s ["",{"text":"Ancient City Chests: ","color":"gold"},{"score":{"name":"@s","objective":"stats_ancient_city_chests"},"bold":true,"color":"gold"}]
tellraw @s ["",{"text":"Buried Treasures: ","color":"dark_aqua"},{"score":{"name":"@s","objective":"stats_buried_treasures"},"bold":true,"color":"dark_aqua"}]

tellraw @s {"text":"                                             ","color":"dark_gray","strikethrough":true}

scoreboard players set @s stats_view 0
scoreboard players enable @s stats_view