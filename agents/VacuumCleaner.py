from agents.Agent import Agent
import math


class VacuumCleaner(Agent):
    def __init__(self, env):
        super().__init__(env)
        self.dirt_collected = 0

    def remove_dirt(self):
        if self.current_position in self.environment.dirts:
            self.environment.dirts.remove(self.current_position)
            self.dirt_collected += 1

    def avoid(self):
        possible_directions = self.possible_directions()
        obstacles = self.environment.obstacles

        possible_directions = {key: value for key, value in possible_directions.items() if value not in obstacles}

        return possible_directions

    def choose_best_action(self):
        # check if the goal is in a possible direction
        if self.environment.set_goal() in self.possible_directions().values():
            return next((k for k, v in self.possible_directions().items() if v == self.environment.set_goal()),
                        None)

        # Avoid obstacles
        possible_directions = self.avoid()

        if not possible_directions:
            # If no possible directions, allow retracing back
            possible_directions.update(self.previous_position)

            if not possible_directions:
                raise ValueError("No possible directions")

        # Choose the action with the minimum distance to the closest dirt
        min_distance = math.inf
        best_action = None

        for direction, pos in possible_directions.items():
            for dirt_pos in self.environment.dirts:
                distance = abs(dirt_pos[0] - pos[0]) + abs(dirt_pos[1] - pos[1])
                if distance < min_distance:
                    min_distance = distance
                    best_action = direction

        return best_action

    def update_memory_with_action(self):
        direction = self.choose_best_action()
        self.update_memory()
        self.action(direction)
        self.send_current_position()
        self.remove_dirt()
