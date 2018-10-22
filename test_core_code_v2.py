from core_code_v2 import distance_between, update
import agentframework
import math


def test_distance_between():
    environment = [0, 0, 0, 0]
    agent1 = [0, 0, 0, 0]
    agent2 = [5, 3, 3, 5]
    agent = agentframework.Agent(environment, agent1)
    agent1_2 = agentframework.Agent(environment, agent2)
    assert distance_between(agent, agent) == 0
    assert distance_between(agent1_2, agent) != 0

def test_update():
    assert update(5) == None
    assert update(0) == None

import pytest
pytest.main()
