import math


class Agent:
    def __init__(self, environment):  # position est tuple (x, y)
        self.environment = environment
        self.current_position = environment.agent_current_position
        self.previous_position = {}
        self.max_memory_size = 4
        self.memory = [self.current_position]  # stores previous positions

    def update_memory(self):  # the agent is a king piece
        self.memory.append(self.current_position)
        if len(self.memory) > self.max_memory_size:
            self.memory = [pos for pos in self.previous_position.values()]

    def possible_directions(self):
        possible_directions = dict()

        if (self.current_position[0] - 1) >= 0:
            possible_directions["up"] = ((self.current_position[0] - 1), self.current_position[1])
        if (self.current_position[0] + 1) < self.environment.size[0]:
            possible_directions["down"] = ((self.current_position[0] + 1), self.current_position[1])
        if (self.current_position[1] - 1) >= 0:
            possible_directions["left"] = (self.current_position[0], (self.current_position[1] - 1))
        if (self.current_position[1] + 1) < self.environment.size[1]:
            possible_directions["right"] = (self.current_position[0], (self.current_position[1] + 1))

        # remove previous position from possible_directions
        if self.memory:
            possible_directions = {key: value for key, value in possible_directions.items() if
                                   value not in self.memory}

        return possible_directions

    def choose_best_action(self):
        # check if the goal is in a possible direction
        if self.environment.set_goal() in self.possible_directions().values():
            return next((k for k, v in self.possible_directions().items() if v == self.environment.set_goal()),
                        None)

        # choix de distance minimal
        if len(self.possible_directions().keys()) >= 1:
            min_distance = math.inf
            best_action = None

            for direction, pos in self.possible_directions().items():
                distance = abs(self.environment.set_goal()[0] - pos[0]) + abs(
                    self.environment.set_goal()[1] - pos[1])

                if distance < min_distance:
                    min_distance = distance
                    best_action = direction
        else:
            raise ValueError("no possible directions")

        return best_action

    def update_memory_with_action(self):
        direction = self.choose_best_action()
        self.update_memory()
        self.action(direction)
        self.send_current_position()

    def action(self, direction):
        if direction == "up":
            self.previous_position["down"] = self.current_position
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
        elif direction == "down":
            self.previous_position["up"] = self.current_position
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        elif direction == "left":
            self.previous_position["right"] = self.current_position
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
        elif direction == "right":
            self.previous_position["left"] = self.current_position
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
        else:
            raise ValueError("Invalid direction")

    def send_current_position(self):
        self.environment.agent_current_position = self.current_position

