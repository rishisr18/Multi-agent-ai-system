# memory/memory_store.py
import json
import time

class MemoryStore:
    def __init__(self, redis_client):
        self.redis = redis_client

    def log(self, parsed_input, file_type, intent):
        entry = {
            "source": file_type,
            "intent": intent,
            "timestamp": time.time(),
            "raw": parsed_input["content"]
        }
        self.redis.set("current_entry", json.dumps(entry))

    def update(self, data: dict):
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                self.redis.set(k, json.dumps(v))
            else:
                self.redis.set(k, str(v))
