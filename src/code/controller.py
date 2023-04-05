import json
from collections import defaultdict
##
from code.models import Agent

class Controller():
    def __init__(self, scenario='./data/scenario_default.json'):
        self.agents = []
        with open(scenario, 'r') as loaded_file:
            scenario_data = json.load(loaded_file)
        self.agents_by_id = {}
        for index, agent_json in enumerate(scenario_data['agents']):
            self.agents.append(Agent.from_json_blob(agent_json))
            self.agents[-1].set_id(index)
            self.agents_by_id[self.agents[-1].ID] = self.agents[-1]
        self.alerts = []
        self.order_agents()
        self.round_number = 1
        self.turn_number = 0
        self.active_agents = self.agents_by_order[1]

    def damaged(self, subject_id, damage, object_id=None):
        self.agents_by_id[subject_id].damaged(damage)
        self.alert_cleanup()

    def alert_cleanup(self):
        for agent in self.agents:
            self.alerts+=agent.alerts
            agent.alerts = []

    def order_agents(self):
        self.agents_by_order = defaultdict(list)
        self.agents = sorted(
            self.agents, 
            key=lambda ag: ag.order_number )
        for agent in self.agents:
            self.agents_by_order[agent.order_number].append(agent)

    def set_new_order(self, ID_list):
        #elements in ID_list might be an int, or a list of ints for agents that share a turn
        agents_modified = set()
        for index, agent_id in enumerate(ID_list):
            order = index+1
            if type(agent_id) == int:
                self.agents_by_id[agent_id].order_number = order
                agents_modified.add(agent_id)
                continue
            for sub_agent in agent_id:
                self.agents_by_id[sub_agent].order_number = order
                agents_modified.add(sub_agent)
        lower_bound = len(agents_modified)
        for index, agent_id in enumerate(self.agents_by_id.keys()):
            if agent_id in agents_modified:
                continue
            self.agents_by_id[agent_id].order_number = index+lower_bound
        self.order_agents()

    def turn_end(self):
        for agent in self.active_agents:
            self.agents_by_id[agent.ID].turn_end()
        self.turn_number += 1
        possible_turns = list(self.agents_by_order.keys())
        if self.turn_number == len(possible_turns):
            self.turn_number = 0
            self.round_number += 1
        self.active_agents = self.agents_by_order[possible_turns[self.turn_number]]



if __name__ == '__main__':
    main()