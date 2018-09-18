import os

cached_agent = None


def jennifer_agent():
    global cached_agent
    if cached_agent is None:
        from .agent import Agent
        cached_agent = Agent()
        Agent.instance = cached_agent
    return cached_agent
