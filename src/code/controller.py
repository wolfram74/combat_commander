import json
import os
import sys
from collections import defaultdict
import time
##
from code.models import Agent

class Controller():

    @classmethod
    def get_agents_from_scenario(cls, address, parent_address=None):
        agents = []
        if parent_address:
            address = os.path.join(os.path.split(parent_address)[0], address)
        with open(address, 'r') as scenario_file:
            scenario_data = json.load(scenario_file)
        if 'agents' in scenario_data:
            for index, agent_json in enumerate(scenario_data['agents']):
                agents.append(Agent.from_json_blob(agent_json))
        if 'files' in scenario_data:
            for sub_address in scenario_data['files']:
                agents += Controller.get_agents_from_scenario(sub_address, parent_address=address)
        return agents

    def __init__(self, scenario='./data/scenario_default.json'):
        self.agents = Controller.get_agents_from_scenario(scenario)
        # with open(scenario, 'r') as loaded_file:
        #     scenario_data = json.load(loaded_file)
        self.agents_by_id = {}
        self.set_agent_ids()
        # for index, agent_json in enumerate(scenario_data['agents']):
        #     self.agents.append(Agent.from_json_blob(agent_json))
        #     self.agents[-1].set_id(index)
        #     self.agents_by_id[self.agents[-1].ID] = self.agents[-1]
        self.alerts = []
        self.order_agents()
        self.round_number = 1
        self.turn_number = 0
        self.turn_start_time = time.time()

    def set_agent_ids(self):
        highest_id = 0
        for agent in self.agents:
            if agent.ID > highest_id:
                highest_id = agent.ID
        for index, agent in enumerate(self.agents):
            if agent.ID == -1:
                agent.set_id(index+1+highest_id)
            self.agents_by_id[agent.ID] = agent

    def damaged(self, subject_id, damage, object_id=None):
        self.agents_by_id[subject_id].damaged(damage)
        self.alert_cleanup()

    def add_condition(self, subject_id, condition):
        self.agents_by_id[subject_id].add_condition(condition)

    def remove_condition(self, subject_id, condition_name):
        self.agents_by_id[subject_id].conditions = filter(
            lambda cond: cond.name != condition_name,
            self.agents_by_id[subject_id].conditions
            )


    def alert_cleanup(self):
        for agent in self.agents:
            self.alerts+=agent.alerts
            agent.alerts = []

    def order_agents(self):
        self.agents_by_order = [[]]
        self.agents = sorted(
            self.agents, 
            key=lambda ag: ag.order_number )
        lowest = self.agents[0].order_number
        for agent in self.agents:
            agent.active = False
            if agent.order_number > lowest:
                self.agents_by_order.append([])
                lowest = agent.order_number
            self.agents_by_order[-1].append(agent)
        self.active_agents = self.agents_by_order[0]
        for agent in self.active_agents:
            agent.active = True


    def set_new_order(self, ID_list):
        #elements in ID_list might be an int, or a list of ints for agents that share a turn
        agents_modified = set()
        for index, agent_id in enumerate(ID_list):
            order = index
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
            self.agents_by_id[agent_id].order_number = lower_bound+1
        self.order_agents()

    def turn_end(self):
        for agent in self.active_agents:
            self.agents_by_id[agent.ID].turn_end()
        self.turn_number += 1
        possible_turns = len(self.agents_by_order)
        if self.turn_number == possible_turns:
            self.turn_number = 0
            self.round_number += 1
        self.active_agents = self.agents_by_order[self.turn_number]
        for agent in self.active_agents:
            agent.active=True
        self.alert_cleanup()




if __name__ == '__main__':
    main()