# Cycles the "food_random" score from 0 to 15

# 1 more point for all players that "food_random" is lower than 14
scoreboard players add @a[scores={food_random=..14}] food_random 1
# Reset "food_random" for all players that "food_random" is already 15 (or more?)
scoreboard players set @a[scores={food_random=14..}] food_random 0
