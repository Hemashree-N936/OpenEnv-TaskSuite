# OpenEnv-TaskSuite

**Meta OpenEnv Hackathon 2026 Submission**  

A lightweight OpenEnv execution environment for evaluating agentic RL agents on **3 realistic office tasks**: Email Triage, Data Cleaning, and Meeting Scheduling. This environment is fully OpenEnv-compatible, deployable on Hugging Face Spaces, and includes a reproducible baseline inference script.

---

## 📝 Motivation

Real-world office automation tasks often require intelligent decision-making across multiple steps. OpenEnv-TaskSuite provides a **standardized, multi-task RL environment** that:

- Simulates realistic human tasks.
- Provides **incremental rewards** for progress, not just success.
- Includes **programmatic graders** for reproducible scoring.
- Supports deployment and evaluation via **Hugging Face Spaces**.

---

## ⚙️ Tasks Overview

### 1. Email Triage (Easy)
- **Objective:** Classify emails correctly (e.g., Work, Personal, Spam).
- **Observation:** List of emails (sender, subject, snippet, timestamp, label) and inbox state.
- **Action Space:** 
  - `classify(email_id, label)`
  - `reply(email_id, text)` (optional)
- **Grader Score (0.0–1.0):** Fraction of emails correctly classified.
- **Reward Function:**  
  - +0.1 per correct classification  
  - −0.05 per incorrect classification  
  - −0.01 per repeated/no-op action  

---

### 2. Data Cleaning (Medium)
- **Objective:** Clean a dataset by fixing missing values and outliers.
- **Observation:** Pandas-like table, schema, missing/outlier info.
- **Action Space:** 
  - `drop_missing(col)`  
  - `impute_mean(col)`  
  - `clip_outliers(col, lo, hi)`  
  - `validate()` (submit cleaned table)
- **Grader Score (0.0–1.0):**  
  `1 − (||S_agent − S_ref||_F / ||S_ref||_F)`
- **Reward Function:**  
  - +0.05 per correctly cleaned column  
  - −0.04 per corrupted column  
  - −0.01 per no-op  

---

### 3. Meeting Scheduling (Hard)
- **Objective:** Schedule meetings respecting participant availability and constraints.
- **Observation:** Participants, calendars, duration, constraints.
- **Action Space:** 
  - `propose_meeting(start, end, participants)`  
  - `edit_proposal(old_id, new_start, new_end)`  
  - `finalize(id)`
- **Grader Score (0.0–1.0):** Fraction of conflicts resolved.
- **Reward Function:**  
  - +0.1 per valid conflict-reducing proposal  
  - −0.08 per invalid proposal  
  - −0.01 per no-op  

---

## 🛠️ OpenEnv Interface

- **Observation, Action, Reward Models:** Defined using **Pydantic**  
- **Methods Implemented:**  
  - `step(action)` → returns `(observation, reward, done, info)`  
  - `reset()` → returns initial observation  
  - `state()` → returns current state  

- **Metadata:** `openenv.yaml` contains environment info and task metadata.
- **Validation:** Run `openenv validate` to ensure compliance.

---

## 🚀 Baseline Inference Script

The environment includes a baseline script using the **OpenAI API**:

```bash
export HF_TOKEN="your_openai_token"
python inference.py
