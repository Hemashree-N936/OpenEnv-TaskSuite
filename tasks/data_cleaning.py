from openenv_models import DataCleaningObs, Reward

class DataCleaningTask:
    def __init__(self):
        self.state_id = 0
        self.table = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": None}
        ]
        self.done = False

    def reset(self):
        self.state_id = 0
        self.done = False
        return DataCleaningObs(table=self.table, schema={"name":"str","age":"int"}, state_id=self.state_id)

    def step(self, action):
        reward = 0.0
        if action.cmd == "impute_mean":
            col = action.args.get("col")
            if col == "age":
                # Simple mean imputation
                ages = [row["age"] for row in self.table if row["age"] is not None]
                mean_age = sum(ages)/len(ages)
                for row in self.table:
                    if row["age"] is None:
                        row["age"] = mean_age
                        reward += 0.05
        self.state_id += 1
        done = self.state_id >= 2
        score = 1.0 if all(row["age"] is not None for row in self.table) else 0.0
        obs = DataCleaningObs(table=self.table, schema={"name":"str","age":"int"}, state_id=self.state_id)
        return obs, Reward(value=reward, score=score), done, {}