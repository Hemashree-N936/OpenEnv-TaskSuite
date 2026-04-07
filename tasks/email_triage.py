from openenv_models import EmailTriageObs, Reward
import random

class EmailTriageTask:
    def __init__(self):
        self.state_id = 0
        self.emails = [
            {"id": "e1", "from": "boss@example.com", "subject": "Urgent", "label": "priority"},
            {"id": "e2", "from": "friend@example.com", "subject": "Hi!", "label": "normal"}
        ]
        self.done = False

    def reset(self):
        self.state_id = 0
        self.done = False
        return EmailTriageObs(emails=self.emails, state_id=self.state_id)

    def step(self, action):
        reward = 0.0
        correct = 0
        for email in self.emails:
            if action.cmd == "classify" and action.args.get("email_id") == email["id"]:
                if action.args.get("label") == email["label"]:
                    reward += 0.1
                    correct += 1
                else:
                    reward -= 0.05
        self.state_id += 1
        done = self.state_id >= len(self.emails)
        score = correct / len(self.emails)
        obs = EmailTriageObs(emails=self.emails, state_id=self.state_id)
        return obs, Reward(value=reward, score=score), done, {}