# Environment configuration for OpenEnv TaskSuite

ENV_NAME = "OpenEnv-TaskSuite"
VERSION = "0.1.0"

CONFIG = {
    "project": ENV_NAME,
    "version": VERSION,
}
from tasks.email_triage import EmailTriageTask
from tasks.data_cleaning import DataCleaningTask
from tasks.meeting_scheduling import SchedulingTask

class OpenEnvTaskSuite:
    def __init__(self):
        self.tasks = {
            "email_triage": EmailTriageTask(),
            "data_cleaning": DataCleaningTask(),
            "meeting_scheduling": SchedulingTask()
        }
        self.current_task = None

    def reset(self, task_name):
        self.current_task = self.tasks[task_name]
        return self.current_task.reset()

    def step(self, action):
        return self.current_task.step(action)

    def state(self):
        return self.current_task