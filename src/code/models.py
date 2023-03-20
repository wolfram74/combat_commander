class Agent():
    def __init__(self, name, max_hp=None, conditions=[]):
        self.name = name
        self.max_hp = max_hp
        self.conditions = conditions

    def turn_end(self):
        for condition in self.conditions:
            if condition.duration == None:
                continue
            if condition.duration > 0:
                condition.duration -= 1
        self.conditions = list(filter(
            lambda x: x.duration != 0,
            self.conditions
            ))

    def add_condition(self, condition):
        self.conditions.append(condition)


class Condition():
    def __init__(self, name, duration = None):
        self.name = name
        self.duration = duration

if __name__ == '__main__':
    main()