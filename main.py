from agents.classifier_agent import ClassifierAgent
from memory.memory_store import MemoryStore
from utils.file_parser import parse_input, parse_pdf
import redis
import sys
import os

# Redis setup
redis_client = redis.Redis(host='localhost', port=6379, db=0)
memory = MemoryStore(redis_client)
classifier = ClassifierAgent(memory)

def process_file(file_path):
    if file_path.endswith(".pdf"):
        parsed_input = parse_pdf(file_path)
    else:
        with open(file_path, "r") as f:
            content = f.read()
        parsed_input = parse_input(content)

    classifier.handle_input(parsed_input)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
    else:
        process_file(sys.argv[1])
