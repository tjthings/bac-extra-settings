execute as @a[advancements={bac_settings:breed_axolotl=true}] run scoreboard players add @s axolotls_bred 1
execute as @a[advancements={bac_settings:breed_axolotl=true}] run advancement revoke @s only bac_settings:breed_axolotl

function bac_settings:team