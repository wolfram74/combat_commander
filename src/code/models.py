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


    def __init__(self, 
            name, max_hp=None, conditions=[], 
            order_number=100, ID=-1,
            **properties):
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
        self.ID = ID

    def turn_end(self):
        self.active = False
        for condition in self.conditions:
            if condition.duration == None:
                continue
            if condition.duration > 0:
                condition.duration -= 1
            if condition.duration == 0:
                self.alerts.append('%s has ended' % condition.name)
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
            if damage < 0:
                return
            self.alerts.append('%s must make concentration check' % self.name)


    def __str__(self):
        template = "{active} {id:=3d}|{name:25}|{current_hp:=3d}/{max_hp:=3d}"
        if len(self.conditions) > 0:
            template += '\n' + (' '*10)
            for condition in self.conditions:
                template += str(condition)+' | '
        act_val = ">>" if self.active else "  "
        return template.format(**{
            "active":act_val,
            "id":self.ID,
            "name":self.name,
            "max_hp":self.max_hp,
            "current_hp":self.current_hp
            })


class Condition():
    @classmethod
    def from_json_blob(cls, blob):
        # print(blob)
        return Condition(**blob)

    def __init__(self, name, duration = None):
        self.name = name
        self.duration = duration

    def __str__(self):
        if self.duration:
            return "{name} ({dur:=3d})".format(name=self.name, dur=self.duration)
        return self.name

if __name__ == '__main__':
    main()