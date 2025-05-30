# agents/classifier_agent.py
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from utils.llm import detect_intent

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.json_agent = JSONAgent(memory)
        self.email_agent = EmailAgent(memory)

    def handle_input(self, parsed_input):
        file_type = parsed_input["type"]
        content = parsed_input["content"]

        intent = detect_intent(file_type, content)
        self.memory.log(parsed_input, file_type, intent)

        if file_type == "json":
            self.json_agent.process(content)
        elif file_type == "email":
            self.email_agent.process(content, intent)
