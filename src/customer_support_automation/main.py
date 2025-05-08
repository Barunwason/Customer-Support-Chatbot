#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from customer_support_automation.crew import CustomerSupportAutomation

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run(inputs):
    """
    Run the crew.
    """
    
    try:
        CustomerSupportAutomation().crew().kickoff(inputs=inputs)
        with open('final_draft.md', 'r') as file:
            content = file.read()
            return content

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train(inputs):
    """
    Train the crew for a given number of iterations.
    """
    try:
        CustomerSupportAutomation().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CustomerSupportAutomation().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(inputs):
    """
    Test the crew execution and returns the results.
    """
    try:
        CustomerSupportAutomation().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

