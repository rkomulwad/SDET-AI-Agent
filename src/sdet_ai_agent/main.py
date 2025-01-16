#!/usr/bin/env python
import sys
import warnings

from sdet_ai_agent.crew import SDETAIAgent
import sys

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    print("****************** Running SDET Agents ************************")
    inputs = {
        'spec_path': './input/petstore-openapi.yaml'
    }
    crew = SDETAIAgent().crew()
    crew.kickoff(inputs=inputs)
    print("****************** Finished Running SDET Agents ************************")
    print(crew.usage_metrics)
