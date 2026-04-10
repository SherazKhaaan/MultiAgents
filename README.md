# MultiAgents

Revision notes for **6CCSACCM Cooperation, Coordination and Multi-agent Systems** (25~26 SEM2 000001).

This repo collects my study materials for the module, organised by week (Weeks 1–11).

## Contents

- **`MultiAgents/notes/`**: written revision notes for each week (`WeekN_notes.md`).
- **`MultiAgents/mcqs/`**: multiple-choice practice questions per week (`WeekN_mcqs.json`).
- **`MultiAgents/flowcharts/`**: flowcharts summarising key concepts, as both JSON and rendered HTML.
- **`MultiAgents/data/WeekN/`**: source materials for each week: lecture slides, lecture notes, tutorial sheets and solutions, video transcripts, and learning objectives.

## Running the MCQ quiz app

The MCQs can be practiced interactively via a Streamlit app (`mcq_app.py`). It auto-discovers any `*/mcqs/Week*_mcqs.json` files in the repo and lets you pick a module and week from the sidebar.

1. Install dependencies (ideally in a virtualenv):

   ```bash
   pip install -r requirements.txt
   ```

2. Launch the app from the repo root:

   ```bash
   streamlit run mcq_app.py
   ```

   Streamlit will open the quiz in your browser (default: http://localhost:8501). Use the sidebar to pick a week, tick your answers, and click **Check Answer** to see feedback and detailed explanations.
