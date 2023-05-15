from Agent import *


class Asperateur(Agent):
    def __init__(self, env):
        super().__init__(env)
        self.dirt_collected = 0

    def remove_dirt(self):
        if self.current_position in self.environnement.dirts:
            self.environnement.dirts.remove(self.current_position)
            self.dirt_collected += 1

    def avoid(self):
        possible_directions = self.possible_directions()

        common_obstacles = set(possible_directions.values()).intersection(self.environnement.obstacles)
        if len(common_obstacles) > 0:
            possible_directions = {key: value for key, value in possible_directions.items() if
                                   value not in common_obstacles}

        if not possible_directions:
            raise ValueError("no possible directions, cannot move")
        else:
            return possible_directions

