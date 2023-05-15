from Environnement import *
from Agent import *
from Asperateur import *

import time
import os

e1 = Environnement((10, 10), (0, 1), (5, 8))
e1.dirts = e1.generate_dirt()  # list of tuples
e1.obstacles = e1.generate_obstacles()  # list of tuples
vaccum = Asperateur(e1)

while not e1.env_is_clean():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Update the environment
    e1.update_view()

    # waits for one second
    time.sleep(1)

    # agent movement

    vaccum.update_memory_with_action()
