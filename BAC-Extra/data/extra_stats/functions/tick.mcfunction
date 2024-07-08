# Trigger
execute as @a if score @s stats_joined matches 1 unless score @s stats_view matches 0 run function extra_stats:view
execute as @a unless score @s stats_joined matches 1 run function extra_stats:join

# Custom Scoreboards
execute as @a[advancements={extra_stats:breed_axolotl=true}] run scoreboard players add @s stats_axolotls_bred 1
execute as @a[advancements={extra_stats:breed_axolotl=true}] run advancement revoke @s only extra_stats:breed_axolotl

execute as @a[advancements={extra_stats:breed_panda=true}] run scoreboard players add @s stats_pandas_bred 1
execute as @a[advancements={extra_stats:breed_panda=true}] run advancement revoke @s only extra_stats:breed_panda

execute as @a[advancements={extra_stats:tame_llama=true}] run scoreboard players add @s stats_llamas_tamed 1
execute as @a[advancements={extra_stats:tame_llama=true}] run advancement revoke @s only extra_stats:tame_llama

execute as @a[advancements={extra_stats:ancient_city=true}] run scoreboard players add @s stats_ancient_city_chests 1
execute as @a[advancements={extra_stats:ancient_city=true}] run advancement revoke @s only extra_stats:ancient_city

execute as @a[advancements={extra_stats:buried_treasure=true}] run scoreboard players add @s stats_buried_treasures 1
execute as @a[advancements={extra_stats:buried_treasure=true}] run advancement revoke @s only extra_stats:buried_treasure