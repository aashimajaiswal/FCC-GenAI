# LangChain
Notes on theory and projects from 9:35:25 to 11:46:21.

Doc: https://python.langchain.com/docs/introduction/
- Langchain is a framework to make GenAI applications using LLM models.
- why prompt template? Don't want user to type in long prompts again and again for different categories.
- Chain: combine different components like LLMs and prompts in a sequence/ chain to make a gen ai end product
- Sequence Chains: Combine multiple chains
- Simple Sequence Chain vs Sequence Chain: Simple one only shows the last output
- Agents usually have autonomy to perform multi-step tasks independently. They can plan, execute, reason, and interact with tools without constant human guidance.
- tool: a function to do something
- env setup
    ```python
    import os
    os.environ['OPENAI_API_KEY'] = "<key>"
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "<key>"
    ```
