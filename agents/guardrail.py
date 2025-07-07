class InputGuardrail:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def apply(self, user_input):
        if self.condition(user_input):
            return self.action(user_input)
        return user_input

class OutputGuardrail:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def apply(self, output):
        if self.condition(output):
            return self.action(output)
        return output
