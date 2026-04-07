from openenv_models import SchedulingObs, Reward

class SchedulingTask:
    def __init__(self):
        self.state_id = 0
        self.participants = ["Alice","Bob"]
        self.calendars = {"Alice": [{"start":"10:00","end":"11:00"}], "Bob":[{"start":"10:30","end":"11:30"}]}
        self.done = False

    def reset(self):
        self.state_id = 0
        self.done = False
        return SchedulingObs(participants=self.participants, calendars=self.calendars, state_id=self.state_id)

    def step(self, action):
        reward = 0.0
        # naive conflict reduction: +0.1 if meeting proposed avoids overlap
        if action.cmd == "propose_meeting":
            reward += 0.1
        self.state_id += 1
        done = self.state_id >= 3
        score = reward
        obs = SchedulingObs(participants=self.participants, calendars=self.calendars, state_id=self.state_id)
        return obs, Reward(value=reward, score=score), done, {}