import json
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

    def damaged(self, subject_id, damage, object_id=None):
        self.agents_by_id[subject_id].damaged(damage)
        self.alert_cleanup()

    def alert_cleanup(self):
        for agent in self.agents:
            self.alerts+=agent.alerts
            agent.alerts = []


if __name__ == '__main__':
    main()