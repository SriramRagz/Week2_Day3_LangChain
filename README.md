
# Week 2 Day 3 – Trace a LangChain App with LangSmith

## Project Overview

This project demonstrates how to build a simple LangChain application using OpenAI's GPT-4o-mini model and monitor its execution using LangSmith tracing.

The application sends three different prompts to the language model in a single run and prints the responses.

## Technologies Used

- Python
- LangChain
- OpenAI GPT-4o-mini
- LangSmith

## Project Structure

```text
Week2_Day3_LangChain/
├── screenshots/
│   ├── 01_langsmith_project_overview.png
│   ├── 02_three_successful_runs.png
│   ├── 03_trace_prompt_response_latency.png
│   └── 04_token_usage_breakdown.png
├── traced_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the following environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="your-langsmith-api-key"
export LANGSMITH_PROJECT="Week2_Day3_LangChain"
```

5. Run the application:

```bash
python traced_app.py
```

## Assignment Tasks Completed

- Created a LangChain application using ChatOpenAI.
- Executed three different prompts in one run.
- Enabled LangSmith tracing using environment variables.
- Verified successful runs in the LangSmith project.
- Inspected prompt, response, latency and token usage.

## LangSmith Trace Evidence

The screenshots folder contains the project overview, successful runs, trace details and token usage breakdown.

## Learning Outcome

This exercise provided practical experience in integrating LangChain with OpenAI and using LangSmith to monitor and understand LLM application execution.

---

**Assignment:** Week 2 – Day 3  
**Project:** Trace a LangChain App with LangSmith
