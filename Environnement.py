from random import *


class Environnement:
    def __init__(self, size, ini_pos):
        self.size = size  # tuple
        self.initial_pos = ini_pos
        self.agent_current_position = ini_pos  # tuple
        self.goal_position = (0, 0)  # tuple
        self.obtacle_ratio = 1 / 5
        self.dirt_ratio = 1 / 5
        self.dirts = []
        self.obstacles = []

    def update_view(self):
        print(" ", "----" * self.size[0])
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if (i, j) == (self.agent_current_position[0], self.agent_current_position[1]):
                    fill = "A"
                elif (i, j) in self.dirts:
                    fill = "D"
                elif (i, j) in self.obstacles:
                    fill = "D"
                elif i == self.goal_position[0] and j == self.goal_position[1]:
                    fill = "G"
                else:
                    fill = " "
                print(" |", fill, end="")

            print(" |")
            print("", "----" * self.size[0])

    def goal_reached(self):
        return self.agent_current_position == self.goal_position

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
                    if (i, j) not in self.generate_dirt():
                        if random() < self.obtacle_ratio:
                            obstacles_positions.append((i, j))
        return obstacles_positions

    def env_is_clean(self):
        return not self.dirts

    def set_goal(self):
        pass