# Trigger
execute as @a if score @s stats_joined matches 1 unless score @s stats_view matches 0 run function extra_stats:view
execute as @a unless score @s stats_joined matches 1 run function extra_stats:join
