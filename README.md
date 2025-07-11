# BCG X GenAI - Financial Chatbot Project

## Project Overview

The simulation was divided into two main tasks:

- **Task 1:** Analyze Microsoft, Apple & Tesla`s financial performance using data from 10-K and 10-Q filings.
- **Task 2:** Build a simple, rule-based chatbot that provides answers to predefined financial questions using the insights derived from Task 1.

---

## Tools & Technologies

- **Python**
- **pandas** – for data wrangling and analysis  
- **matplotlib** and **seaborn** – for data visualization  
- **Google Colab** – development environment  
- No ML models used; chatbot is rule-based with `if-else` logic

---

## Project Structure

bcg-genai-chatbot/

├── BCGDataAnalysis.ipynb # Financial analysis of Microsoft's filings (Task 1)

└── chatbot.py # Rule-based AI chatbot for answering financial queries (Task 2)



## Supported Chatbot Queries

The chatbot can answer the following predefined financial questions:

- What was the total revenue for Microsoft in 2022?
- How has net income of Microsoft changed from 2022 to 2023?
- What were the total assets for Microsoft in 2024?
- What was the revenue growth of Microsoft from 2023 to 2024?
- What is the change in total assets for Microsoft from 2023 to 2024?

All other inputs return a fallback message:  
> “Sorry, I can only provide information on predefined queries.”

---

## What I Learned

- How to simulate a chatbot using rule-based logic (`if-else` structure)
- How to turn raw financial data into actionable, conversational insights
- How to simplify technical outputs for non-technical users

---

## Limitations

- No NLP or AI model integration (only exact-match rule-based logic)
- Chatbot only recognizes predefined queries with exact wording
- Not production-ready (designed as a learning prototype)

---

