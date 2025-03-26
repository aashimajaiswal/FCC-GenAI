# F1 Rules and Regulations ChatBot
- About: Ask the chatbot about 2024 Formula 1 rules and regulations. Source: https://www.fia.com/sites/default/files/fia_2025_formula_1_sporting_regulations_-_issue_1_-_2024-07-31.pdf
- Flow diagram/ Architecture
    - User: Sends in a query to
    - Frontend (Telegram): passes it to
    - Backend (OpenAI): passes it to
    - LLM(some GPT model): Sends back a response to Backend -> Frontend -> User
    - AWS CI/CD to deploy the application

- setup
    - create conda env `$ conda create -n F1RegBot python -y`
    - activate the env `$ conda activate F1RegBot`
    - install requirements `$ pip install -r requirements.txt`
- `/__init__.py`: file tells python that this folder is a package/ module from which you can import methods