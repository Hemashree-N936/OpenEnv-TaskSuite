# Inference utilities for OpenEnv TaskSuite

from openenv_models import Task


def run_task(task: Task):
    print(f"Running task: {task.name}")
    return task.run()
import os, json
from openai import OpenAI
from env import OpenEnvTaskSuite
from openenv_models import Action

client = OpenAI(api_key=os.environ["HF_TOKEN"])
env = OpenEnvTaskSuite()

for task in ["email_triage","data_cleaning","meeting_scheduling"]:
    obs = env.reset(task)
    done = False
    total_reward = 0
    while not done:
        # simplest baseline: random action
        if task == "email_triage":
            act = Action(task=task, cmd="classify", args={"email_id":"e1","label":"priority"})
        elif task == "data_cleaning":
            act = Action(task=task, cmd="impute_mean", args={"col":"age"})
        else:
            act = Action(task=task, cmd="propose_meeting", args={"start":"11:00","end":"12:00","participants":["Alice","Bob"]})
        obs, reward, done, info = env.step(act)
        total_reward += reward.value
    print(f"Task {task}: final score={reward.score}, total_reward={total_reward}")