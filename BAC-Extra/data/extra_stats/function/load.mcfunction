# Initialize Players
scoreboard objectives add stats_joined trigger

# Trigger Command
scoreboard objectives add stats_view trigger

# Custom Scoreboards
scoreboard objectives add stats_axolotls_bred dummy
scoreboard objectives add stats_pandas_bred dummy
scoreboard objectives add stats_llamas_tamed dummy
scoreboard objectives add stats_buried_treasures dummy
scoreboard objectives add stats_ancient_city_chests dummy

execute as @a[advancements={extra_stats:breed_axolotl=true}] run advancement revoke @s only extra_stats:breed_axolotl
execute as @a[advancements={extra_stats:breed_panda=true}] run advancement revoke @s only extra_stats:breed_panda
execute as @a[advancements={extra_stats:tame_llama=true}] run advancement revoke @s only extra_stats:tame_llama
execute as @a[advancements={extra_stats:ancient_city=true}] run advancement revoke @s only extra_stats:ancient_city
execute as @a[advancements={extra_stats:buried_treasure=true}] run advancement revoke @s only extra_stats:buried_treasure