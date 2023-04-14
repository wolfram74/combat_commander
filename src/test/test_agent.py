import unittest
from code.models import Agent, Condition

class TestAgentProperties(unittest.TestCase):
    def setUp(self):
        hasted = Condition(name='hasted', duration=2)
        self.manual_agent = Agent(name='filbert', max_hp = 20, conditions=[hasted])

    def testMeta(self):
        self.assertTrue(True)

    def testCleanUp(self):
        self.assertTrue(
            len(self.manual_agent.conditions)>0
            )
        self.manual_agent.turn_end()
        self.manual_agent.turn_end()
        self.manual_agent.turn_end()
        self.assertTrue(
            len(self.manual_agent.conditions)==0
            )

    def testAddCondition(self):
        self.assertEqual(
            len(self.manual_agent.conditions) , 1
            )
        invis = Condition(name='invisible')
        self.manual_agent.add_condition(invis)
        self.assertEqual(
            len(self.manual_agent.conditions) , 2
            )
        self.manual_agent.turn_end()
        self.manual_agent.turn_end()
        self.manual_agent.turn_end()
        self.assertEqual(
            len(self.manual_agent.conditions) , 1
            )

    def testAgentFromJSON(self):
        json_agent = Agent.from_json_blob({"name":"blobbert", "max_hp":12})
        self.assertEqual(
            json_agent.max_hp , 12
            )


