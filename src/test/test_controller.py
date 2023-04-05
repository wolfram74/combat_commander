import unittest
import os
from code.models import Agent, Condition
from code.controller import Controller

base_directory = os.path.dirname(__file__)
test_scenario1 = os.path.join(base_directory, '../data/scenario_test.json')

class TestController(unittest.TestCase):
    def setUp(self):
        self.loaded_scenario = Controller(scenario = test_scenario1)


    def testCanLoadFromFile(self):
        loaded_scenario = Controller(scenario = test_scenario1)
        self.assertTrue(
            len(loaded_scenario.agents)>0
            )
        self.assertTrue(
            len(loaded_scenario.agents[0].conditions)>0
            )

    def testGivesAgentsIDs(self):
        self.assertEqual(
            type(self.loaded_scenario.agents[0].ID), int
            )

    def testCanTrackDamage(self):
        subject_id = self.loaded_scenario.agents[0].ID
        starting_hp = self.loaded_scenario.agents[0].current_hp
        self.loaded_scenario.damaged(subject_id = subject_id, damage=4)
        self.assertLess(self.loaded_scenario.agents[0].current_hp, starting_hp)

    def testRaisesConcentrationWarning(self):
        subject_id = self.loaded_scenario.agents[1].ID
        starting_hp = self.loaded_scenario.agents[1].current_hp
        self.loaded_scenario.damaged(subject_id = subject_id, damage=4)
        self.assertLess(self.loaded_scenario.agents[1].current_hp, starting_hp)
        self.assertTrue(len(self.loaded_scenario.alerts)>0)
