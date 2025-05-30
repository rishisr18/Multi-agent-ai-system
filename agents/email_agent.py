class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, content, intent):
        lines = content.splitlines()
        sender = next((l.split(":",1)[1].strip() for l in lines if l.lower().startswith("from:")), "unknown")
        urgency = "High" if "urgent" in content.lower() else "Normal"
        self.memory.update({"email_sender": sender, "intent": intent, "urgency": urgency})
