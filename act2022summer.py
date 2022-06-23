from random import randint, choice
from time import sleep
from mcdreforged.api.decorator import new_thread
from mcdreforged.api.types import PluginServerInterface
from mcdreforged.command.builder.nodes.basic import Literal

PLUGIN_METADATA = {
    "id": "act2022summer",
    "version": "1.0.0",
    "name": "TurnA Act 2022 Summer",
    "description": "Helper Plugin",
    "author": "Nyaacinth",
    "dependencies": {
        "mcdreforged": ">=2.0.0"
    }
}

glob_server: PluginServerInterface

food_rain_enabled: bool = False

food_ids = [
    "apple",
    "golden_carrot",
    "cooked_beef",
    "beef",
    "dried_kelp",
    "pumpkin_pie",
    "cookie",
    "bread",
    "honey_bottle",
    "rabbit_stew",
    "mushroom_stew"
]

def enable_food_rain():
    global food_rain_enabled
    food_rain_enabled = True
    tick_food_rain()

@new_thread("foodrain")
def tick_food_rain():
    while food_rain_enabled:
        sleep(1)
        glob_server.execute('execute at @a run summon item ~%d 256 ~%d {Item:{id:"%s",Count:1}}' % (randint(-15, 14), randint(-14, 15), choice(food_ids)))

def disable_food_rain():
    global food_rain_enabled
    food_rain_enabled = False

def on_load(server: PluginServerInterface, prev_module):
    global glob_server
    glob_server = server
    food_rain_ctree = Literal("foodrain")
    food_rain_ctree.then(Literal("start").runs(enable_food_rain))
    food_rain_ctree.then(Literal("stop").runs(disable_food_rain))
    server.register_command(
        Literal("!!act2022summer").then(food_rain_ctree)
    )
