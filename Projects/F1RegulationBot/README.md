# F1 Rules and Regulations ChatBot
- About: Ask the chatbot about 2024 Formula 1 rules and regulations. Source: https://www.fia.com/sites/default/files/fia_2025_formula_1_sporting_regulations_-_issue_1_-_2024-07-31.pdf
- Flow diagram/ Architecture
    - User: Sends in a query to
    - Frontend (Telegram): passes it to
    - Backend (OpenAI): passes it to
    - LLM(some GPT model): Sends back a response to Backend -> Frontend -> User
    - AWS CICD to deploy the application
