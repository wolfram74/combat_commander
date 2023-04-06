class Agent():
    @classmethod
    def from_json_blob(cls, blob):
        conditions = []
        if 'conditions' in blob:
            conditions = list(map(
                lambda condition: Condition.from_json_blob(condition),
                blob['conditions']
                ))
            blob['conditions'] = conditions
        return Agent(**blob)


    def __init__(self, name, max_hp=None, conditions=[], order_number=100, **properties):
        self.name = name
        self.max_hp = max_hp
        if 'current_hp' in properties:
            self.current_hp = properties['current_hp']
        else:
            self.current_hp = self.max_hp
        self.conditions = conditions
        self.order_number = order_number
        self.alerts = []
        self.active = False

    def turn_end(self):
        self.active = False
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

    def set_id(self, id):
        self.ID = id

    def damaged(self, damage):
        self.current_hp -= damage
        if 'concentration' in [cond.name for cond in self.conditions]:
            self.alerts.append('%s must make concentration check' % self.name)



class Condition():
    @classmethod
    def from_json_blob(cls, blob):
        # print(blob)
        return Condition(**blob)

    def __init__(self, name, duration = None):
        self.name = name
        self.duration = duration

if __name__ == '__main__':
    main()