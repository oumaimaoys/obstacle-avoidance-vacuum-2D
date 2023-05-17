import math
from random import *


class Environment:
    def __init__(self, size, ini_pos):
        self.size = size  # tuple (length, width)
        self.initial_pos = ini_pos
        self.agent_current_position = ini_pos  # tuple
        self.obstacle_ratio = 1 / 6
        self.dirt_ratio = 1 / 6
        self.dirts = []
        self.obstacles = []

    def update_view(self):
        print(" ", "----" * self.size[1])
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if (i, j) == (self.agent_current_position[0], self.agent_current_position[1]):
                    fill = "A"
                elif (i, j) in self.dirts:
                    fill = "d"
                elif (i, j) in self.obstacles:
                    fill = "O"
                else:
                    fill = " "
                print(" |", fill, end="")

            print(" |")
            print("", "----" * self.size[1])

    def goal_reached(self):
        return self.agent_current_position == self.set_goal()

    def generate_dirt(self):
        dirt_positions = []
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if (i, j) != self.initial_pos:
                    if random() < self.dirt_ratio:
                        dirt_positions.append((i, j))
        return dirt_positions

    def generate_obstacles(self):
        obstacles_positions = []
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if (i, j) != self.initial_pos:
                    if random() < self.obstacle_ratio:
                        position = (i, j)
                        if position not in self.dirts:  # Check if the position is not already a dirt position
                            obstacles_positions.append(position)

        return obstacles_positions

    def env_is_clean(self):
        return not self.dirts

    def set_goal(self):
        if not self.dirts:
            raise ValueError("No available goal positions. Environment is clean.")

        current_position = self.agent_current_position
        min_distance = math.inf
        closest_dirt = None

        for dirt_pos in self.dirts:
            distance = abs(dirt_pos[0] - current_position[0]) + abs(dirt_pos[1] - current_position[1])

            if distance < min_distance:
                min_distance = distance
                closest_dirt = dirt_pos
        return closest_dirt
