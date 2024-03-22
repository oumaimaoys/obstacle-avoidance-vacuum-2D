from environments.Environment import Environment
from agents.VacuumCleaner import VacuumCleaner
import time
import os

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

length = get_integer_input("Enter the length of the environment: ")
width = get_integer_input("Enter the width of the environment: ")
size = (length, width)

x = get_integer_input("Enter the x coordinate of the initial position: ")
y = get_integer_input("Enter the y coordinate of the initial position: ")
ini_pos = (x, y)

e1 = Environment(size, ini_pos)
e1.dirts = e1.generate_dirt()  # list of tuples
e1.obstacles = e1.generate_obstacles()  # list of tuples
vacuum_cleaner = VacuumCleaner(e1)

# loop until the environment is clean
while not e1.env_is_clean():
    clear_console()
    e1.update_view()
    time.sleep(1)
    vacuum_cleaner.update_memory_with_action()

# final view    
clear_console()
e1.update_view()

print("Dirt collected =", vacuum_cleaner.dirt_collected)
