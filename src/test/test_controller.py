import unittest
import os
from collections import deque

##
from code.models import Agent, Condition
from code.controller import Controller

base_directory = os.path.dirname(__file__)
test_scenario1 = os.path.join(base_directory, '../data/scenario_test.json')
test_scenario2 = os.path.join(base_directory, '../data/scenario_test_ordered.json')
test_scenario3 = os.path.join(base_directory, '../data/scenario_test_recursed.json')

class TestController(unittest.TestCase):
    def setUp(self):
        self.loaded_scenario = Controller(scenario = test_scenario1)
        self.loaded_scenario2 = Controller(scenario = test_scenario2)


    def testCanLoadFromFile(self):
        loaded_scenario = Controller(scenario = test_scenario1)
        self.assertTrue(
            len(loaded_scenario.agents)>0
            )
        self.assertTrue(
            len(loaded_scenario.agents[0].conditions)>0
            )

    def testCanLoadRecursively(self):
        loaded_scenario = Controller(scenario = test_scenario3)
        self.assertTrue(
            len(loaded_scenario.agents)>4
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

    def testAgentsHaveOrder(self):
        self.assertEqual(self.loaded_scenario2.agents_by_order[0][0].name, 'punch kicksmith')

    def testSimpleOrderingCanBeSpecified(self):
        new_order = deque([
                    self.loaded_scenario2.agents[0].ID,   
                    self.loaded_scenario2.agents[1].ID,   
                    self.loaded_scenario2.agents[2].ID,   
                ])
        for i in range(3):
            new_order.rotate()
            self.loaded_scenario2.set_new_order(new_order)
            print(new_order)
            self.assertEqual(
                self.loaded_scenario2.agents_by_order[0][0].name, 
                self.loaded_scenario2.agents_by_id[new_order[0]].name
                )

    def testGroupedOrderingCanBeSpecified(self):
        new_order = [
            [
                self.loaded_scenario2.agents[0].ID,   
                self.loaded_scenario2.agents[1].ID
            ],   
            self.loaded_scenario2.agents[2].ID   
        ]
        self.loaded_scenario2.set_new_order(new_order)
        self.assertEqual(len(self.loaded_scenario2.agents_by_order[0]), 2)

    def testDefaultPositionInOrder(self):
        self.loaded_scenario2.set_new_order(
            [self.loaded_scenario2.agents[0].ID]
            )
        self.assertGreater(
            len(self.loaded_scenario2.agents_by_order[-1]), 1
            )

    def testHasCurrentActiveAgent(self):
        self.assertEqual(len(self.loaded_scenario2.active_agents),1)
        old_active = self.loaded_scenario2.active_agents[0]
        self.loaded_scenario2.turn_end()
        new_active = self.loaded_scenario2.active_agents[0]
        self.assertNotEqual(old_active, new_active)

    def testRoundCounter(self):
        for i in range(9):
            self.loaded_scenario2.turn_end()
        self.assertLess(1,self.loaded_scenario2.round_number)

    def testRemoveCondition(self):
        for i in range(9):
            self.loaded_scenario2.turn_end()
        self.assertLess(1,self.loaded_scenario2.round_number)


