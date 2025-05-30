class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, content):
        required_fields = ["id", "amount"]
        missing = [f for f in required_fields if f not in content]
        self.memory.update({"last_processed": str(content), "missing_fields": missing})
