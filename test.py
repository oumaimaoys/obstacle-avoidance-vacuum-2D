from Environnement import *
from Agent import *

import time
import os

e1 = Environnement((10, 10), (0, 1), (5, 8))
agent = Agent(e1)

while not e1.goal_reached():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Update the environment
    e1.update_view()

    # waits for one second
    time.sleep(1)

    # agent movement

    agent.update_memory_with_action()
